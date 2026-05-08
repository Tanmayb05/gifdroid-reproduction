import os
import json
import re
import pickle
import time
import cv2
import sys
import argparse
from typing import List, Optional
from math import hypot

import openai_api
import gemini_api
from adb_device_controller import ADBDeviceController
from execute_action import execute_actions
import yyh_utils  # Your video/frame utils (SSIM-based segmentation)
from input_formatter import parse_xml_string, label_screenshot, AndroidElement
from dino_detection import run_grounding_dino, annotate_relevant_regions

"""
Main script for segmenting a video of Android UI interaction and replaying those actions on a device.

Supports two boundary-detection algorithms:
  - ssim : pixel-level structural similarity (via yyh_utils)
  - clip : CLIP embedding cosine similarity (via clip_seg)

Usage:
    python segment_replay.py <path_to_video> <boundary_detection_algorithm>
    python segment_replay.py demo.mp4 ssim
    python segment_replay.py demo.mp4 clip
"""

SUPPORTED_ALGORITHMS = ("ssim", "clip")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_json(reply_text):
    """
    Extracts JSON object from GPT reply (removes any markdown formatting).
    """
    reply_text = reply_text.strip()

    # Strip leading/trailing markdown fences
    if reply_text.startswith("```json"):
        reply_text = reply_text[7:]
    elif reply_text.startswith("```"):
        reply_text = reply_text[3:]
    if reply_text.endswith("```"):
        reply_text = reply_text[:-3]

    try:
        return json.loads(reply_text.strip())
    except json.JSONDecodeError:
        pass

    # Fall back: extract the first {...} block from prose responses
    match = re.search(r'\{.*?\}', reply_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    print("❌ JSON decoding failed: no valid JSON found in response")
    raise json.JSONDecodeError("No valid JSON found", reply_text, 0)


def show_images(start_img, stop_img, current_img):
    """
    Displays three images side by side for human inspection (waits for keypress).
    """
    def resize(img, max_height=600):
        h, w = img.shape[:2]
        if h > max_height:
            scale = max_height / h
            return cv2.resize(img, (int(w * scale), max_height))
        return img

    cv2.imshow("Start Frame", resize(start_img))
    cv2.imshow("Stop Frame", resize(stop_img))
    cv2.imshow("Current Frame", resize(current_img))
    print("▶ Press ENTER to continue to the next action, or ESC to exit.")
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if key == 27:
        print("Exiting.")
        sys.exit(0)


def _resolve_region_position(action: dict, region_index_to_center: dict) -> Optional[tuple]:
    """
    Returns a (x, y) center if action["region"] is a valid integer index into region_index_to_center.
    Returns None if region is a list/bbox (LLM hallucination) or unknown index.
    """
    region = action.get("region")
    if isinstance(region, int) and region in region_index_to_center:
        return region_index_to_center[region]
    return None


def match_action_to_element(action: dict, elements: List[AndroidElement]) -> Optional[AndroidElement]:
    """
    Attempts to map an action to the best matching AndroidElement.
    Tries by text, then by proximity to a position if given.
    """
    if "text" in action:
        target_text = action["text"].strip().lower()
        for e in elements:
            if e.text and e.text.strip().lower() == target_text:
                return e
        for e in elements:
            if e.text and target_text in e.text.strip().lower():
                return e

    if "position" in action:
        px, py = action["position"]
        closest_element = min(
            elements,
            key=lambda e: hypot(px - e.center[0], py - e.center[1]),
            default=None,
        )
        return closest_element

    return None


# ---------------------------------------------------------------------------
# Segmentation helpers
# ---------------------------------------------------------------------------

def segment_with_ssim(frames, y_frames, video_stem, cache_folder):
    """Run SSIM-based stable-segment detection (original yyh_utils path)."""
    os.makedirs(cache_folder, exist_ok=True)
    sim_file = os.path.join(cache_folder, f"sim_list_ssim_{video_stem}.pkl")

    if os.path.exists(sim_file):
        with open(sim_file, "rb") as f:
            sim_list = pickle.load(f)
        print("✅ SSIM similarity list loaded from cache.")
    else:
        sim_list = yyh_utils.calculate_sim_seq(y_frames)
        with open(sim_file, "wb") as f:
            pickle.dump(sim_list, f)
        print("📼 SSIM similarity list calculated and saved.")

    segmenter = yyh_utils.VideoStableSegment(
        stable_sim_threshold=0.95,
        stable_interval_threshold=3,
    )
    stable_segments = segmenter.detect_keyframes(sim_list)
    return stable_segments


def segment_with_clip(frames, video_stem, cache_folder,
                      stable_sim_threshold=0.95, stable_interval_threshold=3):
    """Run CLIP-based stable-segment detection."""
    from clip_seg import VideoStableSegmentCLIP

    os.makedirs(cache_folder, exist_ok=True)
    sim_file = os.path.join(cache_folder, f"sim_list_clip_{video_stem}.pkl")

    clip_segmenter = VideoStableSegmentCLIP(
        stable_sim_threshold=stable_sim_threshold,
        stable_interval_threshold=stable_interval_threshold,
    )

    if os.path.exists(sim_file):
        with open(sim_file, "rb") as f:
            sim_list = pickle.load(f)
        print("✅ CLIP similarity list loaded from cache.")
    else:
        # Convert BGR numpy frames → PIL for CLIP
        from PIL import Image
        pil_frames = [Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)) for f in frames]
        sim_list = clip_segmenter.calculate_clip_sim_seq(pil_frames)
        with open(sim_file, "wb") as f:
            pickle.dump(sim_list, f)
        print("📼 CLIP similarity list calculated and saved.")

    stable_segments = clip_segmenter.detect_keyframes(sim_list)
    return stable_segments


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def generate_summary(
    video_stem: str,
    stable_segments: List,
    actions: List[dict],
    output_root: str,
) -> None:
    """
    Generates and saves a video summary to memory.md in the output directory.
    """
    summary_path = os.path.join(output_root, video_stem, "memory.md")

    segment_count = len(stable_segments) - 1
    action_count = len([a for a in actions if a.get("executed")])
    skipped_count = len([a for a in actions if not a.get("executed")])

    summary_lines = [
        f"# Video Summary: {video_stem}",
        "",
        "## Overview",
        f"- **Total Segments**: {segment_count}",
        f"- **Actions Executed**: {action_count}",
        f"- **Actions Skipped**: {skipped_count}",
        "",
        "## Segment Details",
        ""
    ]

    for i, action in enumerate(actions):
        status = "✅ Executed" if action.get("executed") else "⏭️ Skipped"
        action_type = action.get("action", "unknown").upper()
        predicted = action.get("predicted_action", "—")
        reason = action.get("skip_reason", "—") if not action.get("executed") else "—"

        summary_lines.append(f"### Segment {i}")
        summary_lines.append(f"- **Status**: {status}")
        summary_lines.append(f"- **Action Type**: {action_type}")
        summary_lines.append(f"- **Predicted Action**: {predicted}")
        if action.get("executed"):
            summary_lines.append(f"- **Position**: {action.get('position', 'N/A')}")
        else:
            summary_lines.append(f"- **Skip Reason**: {reason}")
        summary_lines.append("")

    summary_lines.extend([
        "## Artifacts",
        f"- Start/Stop frames: `step_*/tmp_start.png`, `step_*/tmp_stop.png`",
        f"- Device screenshots: `step_*/screenshot-0.png`",
        f"- Labeled elements: `step_*/labeled.png`",
        f"- DINO detections: `step_*/dino.png`",
        f"- Relevant regions: `step_*/relevant_regions.png`",
    ])

    with open(summary_path, "w") as f:
        f.write("\n".join(summary_lines))

    print(f"📝 Summary saved to {summary_path}")


def _prepare_device_for_app(device: ADBDeviceController, app_name: str):
    """
    Prepare device for app testing: go to home screen and open the specified app.

    Args:
        device: ADBDeviceController instance
        app_name: Name of app to open (must match key in app_launch_commands.json)
    """
    import json

    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    commands_file = os.path.join(project_root, "src_ViBR", "input", "app_launch_commands.json")

    if not os.path.exists(commands_file):
        print(f"❌ App launch commands file not found: {commands_file}")
        return

    with open(commands_file, 'r') as f:
        app_launch_commands = json.load(f)

    if app_name not in app_launch_commands:
        print(f"❌ App '{app_name}' not found in launch commands")
        return

    print(f"🏠 Going to home screen...")
    device.shell("input keyevent 3")
    time.sleep(1)

    launch_cmd = app_launch_commands[app_name]["launch_command"]
    print(f"🚀 Opening app '{app_name}' with command: {launch_cmd}")
    device.shell(launch_cmd)
    time.sleep(2)

    print(f"✅ App '{app_name}' opened and ready")


def main(
    video_path: str,
    algorithm: str,
    output_root: str = "temp",
    cache_dir: str = "cache",
    interactive: bool = False,
    llm: str = "gemini",
    llm_model: str = "gemini-2.5-pro",
    app_name: Optional[str] = None,
):
    """
    Main entry point: processes video and replays UI actions segment by segment.
    If app_name is provided, goes to home screen and opens the app before starting video replay.
    """
    algorithm = algorithm.lower()
    if algorithm not in SUPPORTED_ALGORITHMS:
        print(f"❌ Unknown algorithm '{algorithm}'. Choose from: {SUPPORTED_ALGORITHMS}")
        sys.exit(1)

    llm = llm.lower()
    if llm == "gemini":
        gemini_api.set_model(llm_model)
        provider = gemini_api
    else:
        provider = openai_api

    print(f"🔹 Starting video processing (algorithm={algorithm}, llm={llm}, model={llm_model})...")
    print("Initializing ADB device controller...")
    device = ADBDeviceController()

    if app_name:
        print(f"📱 Preparing device for app: {app_name}")
        _prepare_device_for_app(device, app_name)

    video_stem = os.path.splitext(os.path.basename(video_path))[0]
    video_out_dir = os.path.join(output_root, video_stem)
    os.makedirs(video_out_dir, exist_ok=True)

    live_path = device.screenshot(index=0, save_path=video_out_dir)

    frames, y_frames = yyh_utils.read_frames_from_video(video_path, header_pixel_size=33)

    # ---- Segment detection (switchable) ----
    print("🔍 Detecting stable segments...")
    if algorithm == "ssim":
        stable_segments = segment_with_ssim(frames, y_frames, video_stem, cache_folder=cache_dir)
    else:
        stable_segments = segment_with_clip(frames, video_stem, cache_folder=cache_dir)

    if stable_segments[0][0] > 2:
        stable_segments = [(0, 1)] + stable_segments

    # ---- Track actions for summary ----
    actions_log = []

    # ---- Per-segment replay loop (unchanged) ----
    for i in range(len(stable_segments) - 1):
        time.sleep(0.5)
        print(f"\n📂 Processing segment {i}...")

        start = min(stable_segments[i][1], len(frames) - 1)
        stop = min(stable_segments[i + 1][0], len(frames) - 1)

        start_img = frames[start]
        stop_img = frames[stop]
        live_path = device.screenshot(index=0, save_path=video_out_dir, filename=f"step_{i}_screenshot-0.png")

        tmp_start_path = os.path.join(video_out_dir, f"step_{i}_tmp_start.png")
        tmp_stop_path = os.path.join(video_out_dir, f"step_{i}_tmp_stop.png")
        cv2.imwrite(tmp_start_path, start_img)
        cv2.imwrite(tmp_stop_path, stop_img)

        # XML UI parse and clickable element detection
        xml_str = device.get_ui_xml()
        elements = parse_xml_string(xml_str, bound_margin=10, min_cent_dist=20, clickable_only=True)
        if len(elements) <= 5:
            elements = parse_xml_string(xml_str, bound_margin=10, min_cent_dist=20)

        labeled_path = label_screenshot(
            screenshot_path=live_path,
            screenshot_dir=video_out_dir,
            name=f"step_{i}_labeled",
            elements=elements,
        )
        current_img_labeled_xml_region = cv2.imread(labeled_path)

        # DINO detection for grounding region proposals
        dino_out_path = os.path.join(video_out_dir, f"step_{i}_dino.png")
        dino_regions = run_grounding_dino(tmp_start_path, dino_out_path)

        regions = []
        for idx, e in enumerate(elements):
            region = {
                "index": idx,
                "center": e.center,
                "box": list(e.bounds),
                "phrase": e.text if e.text else "unknown element",
            }
            regions.append(region)

        relevant = provider.ask_gpt_for_relevant_regions(dino_out_path, tmp_stop_path)
        relevant = extract_json(relevant)
        print(f"🔍 Relevant regions: {relevant}")
        target_indices = relevant["target_regions"]
        print(f"🧠 GPT selected regions: {target_indices}")

        relevant_annotated_path = os.path.join(video_out_dir, f"step_{i}_relevant_regions.png")
        annotate_relevant_regions(tmp_start_path, relevant_annotated_path, dino_regions, target_indices)

        region_index_to_center = {r["index"]: r["center"] for r in regions}

        if interactive:
            show_images(
                cv2.imread(relevant_annotated_path),
                stop_img,
                current_img_labeled_xml_region,
            )

        match = extract_json(
            provider.ask_gpt_state_consistency(
                relevant_annotated_path, live_path,
                relevant["predicted_action"], relevant["target_regions"],
            )
        )

        attempts = 0
        max_attempts = 3
        while match["same_state"] != "yes" and attempts < max_attempts:
            print(f"🔄 Attempting to align state (try {attempts + 1}/{max_attempts})...")
            elements = parse_xml_string(xml_str, bound_margin=10, min_cent_dist=20, clickable_only=True)
            if len(elements) <= 5:
                elements = parse_xml_string(xml_str, bound_margin=10, min_cent_dist=20)

            labeled_path = label_screenshot(
                screenshot_path=live_path,
                screenshot_dir=video_out_dir,
                name=f"step_{i}_labeled",
                elements=elements,
            )

            recovery_reply = provider.ask_gpt_for_action_region(
                tmp_start_path, tmp_stop_path, labeled_path, relevant["predicted_action"],
            )
            recovery_action = extract_json(recovery_reply)

            pos = _resolve_region_position(recovery_action, region_index_to_center)
            if pos is not None:
                recovery_action["position"] = pos
                print(f"🎯 Recovery using region index: {recovery_action['region']} at {pos}")
            else:
                matched_element = match_action_to_element(recovery_action, elements)
                if matched_element:
                    recovery_action["position"] = matched_element.center
                    print(f"🎯 Recovery matched element: '{matched_element.text}' at {matched_element.center}")

            position_required = recovery_action.get("action") in ("tap", "double_tap", "long_press")
            if position_required and "position" not in recovery_action:
                print("⚠️ Recovery: no position resolved, skipping action.")
                attempts += 1
                continue

            execute_actions(device, [recovery_action])
            time.sleep(1.0)
            live_path = device.screenshot(index=0, save_path=video_out_dir, filename=f"step_{i}_screenshot-0.png")
            match = extract_json(provider.ask_gpt_state_consistency(tmp_start_path, live_path))
            attempts += 1

        if match["same_state"] == "yes":
            reply = provider.ask_gpt_for_action_region(
                relevant_annotated_path, tmp_stop_path, labeled_path,
                relevant["predicted_action"], target_indices,
            )
            action = extract_json(reply)

            matched_element = match_action_to_element(action, elements)
            pos = _resolve_region_position(action, region_index_to_center)
            if pos is not None:
                action["position"] = pos
                print(f"🎯 Using region index: {action['region']} at {pos}")
            elif matched_element:
                action["position"] = matched_element.center
                print(f"🎯 Matched element: '{matched_element.text}' at {matched_element.center}")
            else:
                position_required = action.get("action") in ("tap", "double_tap", "long_press")
                if position_required:
                    print("⚠️ No valid region or element match. Skipping action.")
                    actions_log.append({
                        "segment": i,
                        "executed": False,
                        "predicted_action": relevant["predicted_action"],
                        "skip_reason": "No valid region or element match",
                    })
                    continue
                print("⚠️ No valid region or element match. Proceeding without position.")

            execute_actions(device, [action])
            actions_log.append({
                "segment": i,
                "executed": True,
                "action": action.get("action"),
                "position": action.get("position"),
                "predicted_action": relevant["predicted_action"],
            })
            print("✅ Action executed.\n")
        else:
            print(
                "⚠️ Skipping action: current GUI state does not match start state.\n"
                f"Mismatch reason: {match['description']}"
            )
            actions_log.append({
                "segment": i,
                "executed": False,
                "predicted_action": relevant["predicted_action"],
                "skip_reason": match.get("description", "GUI state mismatch"),
            })

        if interactive:
            input("Press Enter to continue...")

    print("✅ Video processing completed.")
    generate_summary(video_stem, stable_segments, actions_log, output_root)

    # Export metrics for main.py
    from collections import Counter
    action_types = Counter(action.get("type", "unknown") for action in actions_log)
    metrics_data = {
        "total_scenes": len(stable_segments) - 1,
        "scenes_processed": len(actions_log),
        "scenes_failed": 0,
        "action_types": dict(action_types),
        "llm_calls": getattr(provider, "llm_calls", []) if hasattr(provider, "llm_calls") else [],
    }
    metrics_path = os.path.join(output_root, "vibr_metrics.json")
    import json
    with open(metrics_path, "w") as f:
        json.dump(metrics_data, f, indent=2, default=str)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Segment and replay actions from video.")
    parser.add_argument("video_path", type=str, help="Path to the input video")
    parser.add_argument(
        "algorithm",
        type=str,
        default="clip",
        choices=SUPPORTED_ALGORITHMS,
        help="Boundary detection algorithm: ssim or clip",
    )
    parser.add_argument(
        "--output-root",
        type=str,
        default="temp",
        help="Directory where replay artifacts are written.",
    )
    parser.add_argument(
        "--cache-dir",
        type=str,
        default="cache",
        help="Directory where similarity cache (.pkl) files are stored.",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Show OpenCV windows and pause between actions.",
    )
    parser.add_argument(
        "--llm",
        type=str,
        default="gemini",
        choices=("openai", "gemini"),
        help="LLM provider to use for visual reasoning (default: gemini).",
    )
    parser.add_argument(
        "--llm-model",
        type=str,
        default="gemini-2.5-pro",
        help="Model name for the selected LLM provider (default: gemini-2.5-pro).",
    )
    parser.add_argument(
        "--app-name",
        type=str,
        default=None,
        help="App name to open at the start (optional). Will go home then open app before video replay.",
    )
    args = parser.parse_args()
    main(
        args.video_path,
        args.algorithm,
        output_root=args.output_root,
        cache_dir=args.cache_dir,
        interactive=args.interactive,
        llm=args.llm,
        llm_model=args.llm_model,
        app_name=args.app_name,
    )
