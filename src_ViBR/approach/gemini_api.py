import base64
import json
import os
import time
from pathlib import Path
from urllib import error as url_error, request as url_request

"""
Functions to interact with Google Gemini for visual app state comparison, action region prediction,
and relevant region identification for Android GUI screenshots.

Mirrors the openai_api.py interface — functions have identical signatures so segment_replay.py
can swap providers with a simple module-level import.

Auth (in priority order):
  1. GOOGLE_GENERATIVE_AI_API_KEY env var or .env.local → Google AI Studio endpoint
  2. Application Default Credentials (ADC) → Vertex AI endpoint
     Optional: GEMINI_VERTEX_PROJECT_ID, GEMINI_VERTEX_LOCATION (default: us-central1)
"""

_DEFAULT_MODEL = "gemini-1.5-flash"
_MODEL: str | None = None  # overridden by set_model()
llm_calls: list[dict] = []  # Track all LLM API calls for metrics


def set_model(model: str) -> None:
    """Set the Gemini model name to use for all calls in this process."""
    global _MODEL
    _MODEL = model


def _get_model() -> str:
    return _MODEL if _MODEL else _DEFAULT_MODEL


# ---------------------------------------------------------------------------
# Auth / env helpers
# ---------------------------------------------------------------------------

def _load_env_local(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export "):].strip()
        if "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key:
            values[key] = val
    return values


def _get_env() -> dict[str, str]:
    repo_root = Path(__file__).resolve().parents[2]
    env_values = _load_env_local(repo_root / ".env.local")
    merged = {**env_values, **{k: v for k, v in os.environ.items() if v}}
    return merged


def _build_url_and_headers(model: str) -> tuple[str, dict[str, str]]:
    env = _get_env()
    api_key = env.get("GOOGLE_GENERATIVE_AI_API_KEY", "").strip()
    headers = {"Content-Type": "application/json"}

    if api_key:
        url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent?key={api_key}"
        )
        return url, headers

    # Fall back to ADC / Vertex AI
    try:
        import google.auth
        from google.auth.transport.requests import Request as GoogleRequest
    except ImportError as exc:
        raise RuntimeError(
            "google-auth is required for Gemini ADC auth. "
            "Install it with: pip install google-auth"
        ) from exc

    try:
        creds, project_id = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        creds.refresh(GoogleRequest())
    except Exception as exc:
        raise RuntimeError(
            "Failed to load Application Default Credentials. "
            "Set GOOGLE_GENERATIVE_AI_API_KEY in .env.local, "
            "run `gcloud auth application-default login`, "
            "or set GOOGLE_APPLICATION_CREDENTIALS."
        ) from exc

    token = getattr(creds, "token", None)
    if not token:
        raise RuntimeError("ADC token refresh returned empty token.")

    vertex_project = (
        env.get("GEMINI_VERTEX_PROJECT_ID", "").strip() or str(project_id or "")
    )
    if not vertex_project:
        raise RuntimeError(
            "ADC did not provide a project_id and GEMINI_VERTEX_PROJECT_ID is not set."
        )
    location = env.get("GEMINI_VERTEX_LOCATION", "us-central1").strip() or "us-central1"

    url = (
        f"https://{location}-aiplatform.googleapis.com/v1/"
        f"projects/{vertex_project}/locations/{location}/publishers/google/models/"
        f"{model}:generateContent"
    )
    headers["Authorization"] = f"Bearer {token}"
    return url, headers


# ---------------------------------------------------------------------------
# HTTP call with retry
# ---------------------------------------------------------------------------

_MAX_RETRIES = 5
_BASE_DELAY = 10  # seconds
_DEFAULT_TIMEOUT = 180  # seconds — increased for slower models like gemini-2.5-pro


def _call_gemini(parts: list[dict], timeout: int = _DEFAULT_TIMEOUT, kind: str = "unknown") -> str:
    model = _get_model()
    url, headers = _build_url_and_headers(model)

    payload = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {"temperature": 0.1},
    }
    payload_bytes = json.dumps(payload).encode("utf-8")

    call_start = time.time()
    error = None
    prompt_tokens = 0
    output_tokens = 0

    for attempt in range(_MAX_RETRIES):
        req = url_request.Request(url=url, data=payload_bytes, headers=headers, method="POST")
        try:
            with url_request.urlopen(req, timeout=timeout) as resp:
                response_text = resp.read().decode("utf-8")
            break
        except url_error.HTTPError as exc:
            if exc.code == 429 and attempt < _MAX_RETRIES - 1:
                delay = _BASE_DELAY * (2 ** attempt)
                print(f"Gemini rate limit (429). Retrying in {delay}s...")
                time.sleep(delay)
            else:
                body = exc.read().decode("utf-8", errors="replace")
                error = f"HTTP {exc.code}"
                raise RuntimeError(f"Gemini HTTP error {exc.code}: {body[:300]}") from exc
        except url_error.URLError as exc:
            if isinstance(exc.reason, TimeoutError) and attempt < _MAX_RETRIES - 1:
                delay = _BASE_DELAY * (2 ** attempt)
                print(f"Gemini request timed out (attempt {attempt + 1}/{_MAX_RETRIES}). Retrying in {delay}s...")
                time.sleep(delay)
            else:
                error = str(exc)
                raise RuntimeError(f"Gemini URL error: {exc}") from exc
        except TimeoutError:
            if attempt < _MAX_RETRIES - 1:
                delay = _BASE_DELAY * (2 ** attempt)
                print(f"Gemini request timed out (attempt {attempt + 1}/{_MAX_RETRIES}). Retrying in {delay}s...")
                time.sleep(delay)
            else:
                error = f"Timeout after {_MAX_RETRIES} attempts"
                raise RuntimeError(f"Gemini request timed out after {_MAX_RETRIES} attempts ({timeout}s each)")

    elapsed_sec = time.time() - call_start

    data = json.loads(response_text)
    candidates = data.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise RuntimeError(f"Gemini returned no candidates: {response_text[:300]}")
    parts_out = candidates[0].get("content", {}).get("parts", [])
    if not parts_out:
        raise RuntimeError(f"Gemini candidate has no parts: {response_text[:300]}")

    # Extract token counts from response
    usage = data.get("usageMetadata", {})
    prompt_tokens = usage.get("promptTokenCount", 0)
    output_tokens = usage.get("candidatesTokenCount", 0)

    # Record metrics
    llm_calls.append({
        "kind": kind,
        "elapsed_sec": elapsed_sec,
        "prompt_tokens": prompt_tokens,
        "output_tokens": output_tokens,
        "error": error,
    })

    return parts_out[0].get("text", "")


# ---------------------------------------------------------------------------
# Image encoding helper
# ---------------------------------------------------------------------------

def _encode_image(image_path: str) -> str:
    print(image_path)
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def _image_part(image_path: str) -> dict:
    return {
        "inlineData": {
            "mimeType": "image/png",
            "data": _encode_image(image_path),
        }
    }


# ---------------------------------------------------------------------------
# ViBR inference calls (same signatures as openai_api.py)
# ---------------------------------------------------------------------------

def ask_gpt_state_consistency(start_img, live_img, action="", target_region=""):
    """
    Compares two Android screenshots to determine if their UI state is functionally equivalent,
    using Gemini via the Google Generative AI REST API.

    Args:
        start_img (str): Path to reference image.
        live_img (str): Path to live/current image.
        action (str): The action to check for (optional).
        target_region (str): Target UI region (optional).

    Returns:
        str: Gemini response in JSON: {"same_state": "yes"} or {"same_state": "no", ...}
    """
    prompt = (
        "You are given two screenshots of an Android interface:\n"
        "1. The first image is the REFERENCE state from a stable app video.\n"
        "2. The second image is the CURRENT real-time app state.\n"
        "\n"
        "You also get a possible action and region that has to be executed to reach the target state. "
        "Take this into account but also keep in mind that something else could be the action.\n"
        f"Action: {action}\n Region: {target_region}"
        "Your task is to determine if the current screen is functionally consistent with the reference.\n"
        "That means: Can the user perform the same action from the current screen as in the reference?\n"
        "\n"
        "- Minor differences in layout, text alignment, icon position or additional items that do not "
        "influence the action DO NOT matter.\n"
        "- For home screens or app drawers, the presence of extra app icons, widgets, or a different "
        "order of icons DOES NOT matter, as long as the same action can be performed from both screens.\n"
        "- Focus on whether the same buttons, inputs, or menus are present and usable. Sometimes the "
        "keyboard or something can block some parts, this still means the state is consistent.\n"
        "- Ignore small stylistic or timing variations (e.g., animation state, different time shown, "
        "small icon differences).\n"
        "- Cases like the home screen or similar, where icons can be ordered differently do not matter "
        "if the same action can be performed.\n"
        "\n"
        "Respond strictly in the following JSON format:\n"
        '{ "same_state": "yes" } or { "same_state": "no", "description": "<reason>" }'
    )

    parts = [
        {"text": prompt},
        _image_part(start_img),
        _image_part(live_img),
    ]
    response = _call_gemini(parts, kind="state_comparison")
    print("Consistency Response from Gemini:", response)
    return response.strip().lower()


def ask_gpt_for_action_region(start_img, stop_img, live_img, predicted_action, relevant_indices=None):
    """
    Uses Gemini to infer which action and UI region should be executed on the current (live) screen
    to reproduce a state transition observed in start/stop images.

    Args:
        start_img (str): Path to start image.
        stop_img (str): Path to stop image (after action).
        live_img (str): Path to live/current image.
        predicted_action (str): Action type (e.g., tap, swipe).
        relevant_indices (list): Optionally, region indices.

    Returns:
        str: JSON response from Gemini describing action and region.
    """
    prompt = f"""
    Your goal is to reproduce the action {predicted_action} from the GUI recording on a real device. I show you the three GUI screenshots by order. In the recording, the interaction with the highlighted purple region in the first GUI leads to the second GUI. The current GUI on your device is shown as the third GUI, on which element should you perform the action to achieve the same transition? Please follow the primitive in action space.

    ### Possible Actions:
    1. **tap** - Taps a location on screen. - Example: {{ "action": "tap", "region": 2, "description": "Tap center of screen to open app." }}

    2. **swipe** - Swipes from one point to another. - Example: {{ "action": "swipe", "from": [540, 1600], "to": [540, 400], "duration": 500, "description": "Swipe up to scroll." }}

    3. If you see the keyboard on the GUI screen, it is highly possible is a **input_text** - Types text into a focused input field. - Example: {{ "action": "input_text", "text": "hello world", "description": "Type search query." }}

    4. **back** - Presses Android back button. - Example: {{ "action": "back", "description": "Go back to previous screen." }}

    5. **home** - Goes to Android home screen. - Example: {{ "action": "home", "description": "Return to home." }}

    6. **wait** - Waits for a specified duration. - Example: {{ "action": "wait", "duration": 1500, "description": "Wait for animation to finish." }}

    7. **no action** - No action is needed. - Example: {{ "action": "no action", "description": "No Action needed." }}

    Return a **JSON object** describing the required action. Do not include any other text or explanation.
    """

    parts = [
        {"text": prompt},
        _image_part(start_img),
        _image_part(stop_img),
        _image_part(live_img),
    ]
    response = _call_gemini(parts, kind="action_inference")
    print("Region Action Response from Gemini:", response)
    return response.strip()


def ask_gpt_for_relevant_regions(start_img_path, stop_img_path):
    """
    Sends start and stop images to Gemini and asks which UI regions are most relevant for
    the transition, and predicts the action type.

    Args:
        start_img_path (str): Path to start (reference) image.
        stop_img_path (str): Path to stop (after interaction) image.

    Returns:
        str: JSON response with relevant regions and predicted action.
    """
    prompt = """
      You are given two screenshots of an Android interface:

      1. The first image is the REFERENCE state before an interaction.
      2. The second image is the FOLLOW-UP state after the interaction.

      You are also given a list of **interactive UI regions** detected in the reference image. Each region includes:
      - A numeric index
      - A bounding box
      - A phrase describing the region (e.g., "button", "text field")

      Your task is to determine which of these regions are **most likely involved** in the transition between the two states.

      - Focus on regions that, if interacted with, could explain the visual change between the first and second image.
      - Minor layout shifts or content changes are not enough — identify only regions that are plausible interaction targets.
      - Use the phrases and bounding boxes to reason about the intent of the user.
      - When pointers or animations on a button or similar can be seen prioritize the region around it.

      You must also predict the type of user action that caused the change. Choose only from the following actions:
      ["tap", "double_tap", "long_press", "swipe", "input_text", "back", "home", "wait", "no action"]

      Respond strictly in the following JSON format — do not include any other text or explanation. If no regions are relevant, return an empty list:
      { "target_regions": [int, int, ...], "predicted_action": "<action>" }
      """

    parts = [
        {"text": prompt + "\n\nScreenshots are attached below."},
        _image_part(start_img_path),
        _image_part(stop_img_path),
    ]
    response = _call_gemini(parts, kind="region_detection")
    print("Relevant Region Response from Gemini:", response)
    return response.strip()
