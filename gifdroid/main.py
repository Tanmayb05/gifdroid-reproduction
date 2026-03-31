import argparse
import glob
import os
import json
import logging
import time
from datetime import datetime

import cv2

from gifdroid.location import keyframe_location
from gifdroid.hhv_keyframe import get_keyframe_fn
from gifdroid.mapping import gui_mapping
from gifdroid.trace import find_execution_trace

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

def setup_logger(log_dir, video_type='', method='', run_id=None):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
    if run_id:
        run_num = run_id[len('run-'):] if run_id.startswith('run-') else run_id
        log_file = os.path.join(log_dir, f'{timestamp}__run-{run_num}__pipeline__started.log')
    else:
        suffix = f'_{video_type}' if video_type else ''
        suffix += f'_{method}' if method else ''
        log_file = os.path.join(log_dir, f'gifdroid_{timestamp}{suffix}.log')

    fmt = '%(asctime)s  %(levelname)-8s  %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    logging.basicConfig(
        level=logging.DEBUG,
        format=fmt,
        datefmt=datefmt,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger('gifdroid')
    logger.info(f'Log file: {log_file}')
    return logger


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description='GIFdroid: Automated Replay of Visual Bug Reports for Android Apps'
    )
    parser.add_argument('--video', dest='video',
                        help='bug recording',
                        default=None, type=str)
    parser.add_argument('--utg', dest='utg',
                        help='GUI transition graph in json format',
                        default=None, type=str)
    parser.add_argument('--artifact', dest='artifact',
                        help='GUI screenshots in UTG',
                        default=None, type=str)
    parser.add_argument('--out', dest='out',
                        help='output of the execution trace',
                        default='execution.json', type=str)
    parser.add_argument('--log-dir', dest='log_dir',
                        help='directory for log files (default: utg dir derived from --out)',
                        default=None, type=str)
    parser.add_argument('--save-keyframes', dest='save_keyframes',
                        help='directory to save extracted keyframe PNGs (default: <out_dir>/keyframes)',
                        default=None, type=str)
    parser.add_argument('--keyframe-method', dest='keyframe_method',
                        choices=['baseline', 'stabilize', 'hysteresis', 'homography', 'clip', 'vlm'],
                        default='baseline',
                        help='Keyframe detection method (default: baseline)')
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Graph helpers
# ---------------------------------------------------------------------------

def read_graph_with_action(utg):
    with open(utg, 'r') as f:
        parsed_json = json.loads(f.read())
    graph = []
    for event in parsed_json['events']:
        if 'sourceScreenId' not in event or 'destinationScreenId' not in event:
            continue
        s = int(event['sourceScreenId'])
        d = int(event['destinationScreenId'])
        if 'target' in event.keys():
            action_type = event['target']['type']
            action_id = event['target']['targetDetails']
        else:
            action_type = 'LAUNCH'
            action_id = 'app'
        graph.append([s, d, action_type, action_id])
    return graph


def store_trace(utg, traces, out, logger):
    graph = read_graph_with_action(utg)
    output_json = {
        'video': args.video,
        'utg': args.utg,
        'artifact': args.artifact,
        'replay_traces': [],
    }

    for trace in traces:
        trace_seq = {'trace': []}
        for i in range(len(trace) - 1):
            action = None
            for g in graph:
                if g[0] == trace[i] and g[1] == trace[i + 1]:
                    action = g
                    break
            if action is None:
                logger.warning(
                    f'No graph edge found for transition {trace[i]} -> {trace[i+1]}'
                )
                continue
            seq = {
                'sourceScreenId': trace[i],
                'destinationScreenId': trace[i + 1],
                'action': {
                    'type': action[2],
                    'targetDetails': action[3],
                },
            }
            trace_seq['trace'].append(seq)
        output_json['replay_traces'].append(trace_seq)

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, 'w') as fp:
        json.dump(output_json, fp, indent=4)
    logger.info(f'Execution trace written to: {out}')


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def save_keyframes(keyframes, keyframe_indices, save_dir, logger):
    os.makedirs(save_dir, exist_ok=True)
    for i, (frame, idx) in enumerate(zip(keyframes, keyframe_indices)):
        path = os.path.join(save_dir, f'kf-{i+1:04d}.png')
        cv2.imwrite(path, frame)
    logger.info(f'  Keyframes saved to: {save_dir} ({len(keyframes)} files)')


def main(video, screenshots, utg, logger, execution_out=None, keyframes_dir=None, keyframe_method='baseline'):
    total_start = time.time()

    # ------------------------------------------------------------------
    # Step 1: Keyframe location
    # ------------------------------------------------------------------
    logger.info('=' * 50)
    logger.info('STEP 1: Keyframe Location')
    logger.info(f'  Input video      : {video}')
    logger.info(f'  Keyframe method  : {keyframe_method}')
    step_start = time.time()

    keyframe_fn = get_keyframe_fn(keyframe_method)
    keyframe_sequence, keyframe_index = keyframe_fn(video)

    elapsed = time.time() - step_start
    logger.info(f'  Keyframes found   : {len(keyframe_index)}')
    logger.info(f'  Keyframe indices  : {keyframe_index}')
    logger.info(f'  Duration          : {elapsed:.2f}s')

    # ------------------------------------------------------------------
    # Save keyframes to disk
    # ------------------------------------------------------------------
    if keyframes_dir is not None:
        save_keyframes(keyframe_sequence, keyframe_index, keyframes_dir, logger)

    # ------------------------------------------------------------------
    # Step 2: GUI mapping
    # ------------------------------------------------------------------
    logger.info('=' * 50)
    logger.info('STEP 2: GUI Mapping')
    logger.info(f'  Screenshots dir : {screenshots}')
    step_start = time.time()

    index_sequence = gui_mapping(screenshots, keyframe_sequence)

    elapsed = time.time() - step_start
    logger.info(f'  Mapped index sequence : {index_sequence}')
    logger.info(f'  Duration              : {elapsed:.2f}s')

    # ------------------------------------------------------------------
    # Step 3: Execution trace search
    # ------------------------------------------------------------------
    logger.info('=' * 50)
    logger.info('STEP 3: Find Execution Trace')
    logger.info(f'  UTG file : {utg}')
    step_start = time.time()

    traces = find_execution_trace(utg, index_sequence)

    elapsed = time.time() - step_start
    logger.info(f'  Candidate traces found : {len(traces)}')
    for idx, t in enumerate(traces):
        logger.info(f'    Trace {idx}: {t}')
    logger.info(f'  Duration : {elapsed:.2f}s')

    # ------------------------------------------------------------------
    # Step 4: Store trace
    # ------------------------------------------------------------------
    logger.info('=' * 50)
    logger.info('STEP 4: Store Execution Trace')
    step_start = time.time()

    store_trace(utg, traces, execution_out or 'execution_trace.json', logger)

    elapsed = time.time() - step_start
    logger.info(f'  Duration : {elapsed:.2f}s')

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    total_elapsed = time.time() - total_start
    logger.info('=' * 50)
    logger.info(f'Pipeline complete.  Total time: {total_elapsed:.2f}s')
    logger.info('=' * 50)

    return index_sequence, traces


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    args = parse_args()

    # Determine run directory and execution trace output path.
    # --out can be either:
    #   a) a directory path (new structure): run_dir/execution_trace.json is written inside
    #   b) a .json file path (legacy): used directly, run_dir derived as its parent
    out_path = os.path.abspath(args.out)
    if out_path.endswith('.json'):
        execution_out = out_path
        run_dir = os.path.dirname(out_path)
    else:
        run_dir = out_path
        execution_out = os.path.join(run_dir, 'execution_trace.json')

    log_dir = args.log_dir if args.log_dir else os.path.join(run_dir, 'logs')

    # Detect video type from filename
    video_basename = os.path.basename(args.video) if args.video else ''
    if 'hhv' in video_basename:
        video_type = 'hhv'
    elif 'srv' in video_basename:
        video_type = 'srv'
    else:
        video_type = ''

    # Determine run_id from the run directory name if it matches run-NNN pattern
    run_dir_name = os.path.basename(run_dir)
    run_id = run_dir_name if run_dir_name.startswith('run-') else None

    logger = setup_logger(log_dir, video_type, args.keyframe_method, run_id=run_id)

    keyframes_dir = args.save_keyframes if args.save_keyframes else \
        os.path.join(run_dir, 'keyframes')

    logger.info('GIFdroid started')
    logger.info(f'  --video            : {args.video}')
    logger.info(f'  --utg              : {args.utg}')
    logger.info(f'  --artifact         : {args.artifact}')
    logger.info(f'  --out              : {args.out}')
    logger.info(f'  --log-dir          : {args.log_dir}')
    logger.info(f'  --save-keyframes   : {keyframes_dir}')
    logger.info(f'  --keyframe-method  : {args.keyframe_method}')

    if args.video is None or args.utg is None or args.artifact is None:
        logger.error('Missing required arguments. Run with -h for usage.')
        exit(1)

    # Idempotency check: skip if the output trace already exists
    if os.path.isfile(execution_out):
        logger.info(f'Output already exists, skipping: {execution_out}')
        exit(0)

    main(args.video, args.artifact, args.utg, logger, execution_out=execution_out,
         keyframes_dir=keyframes_dir, keyframe_method=args.keyframe_method)
