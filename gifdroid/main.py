import argparse
import glob
import os
import json
import logging
import time
from datetime import datetime

import cv2

from gifdroid.location import keyframe_location
from gifdroid.mapping import gui_mapping
from gifdroid.trace import find_execution_trace

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

def setup_logger(log_dir, video_type=''):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    suffix = f'_{video_type}' if video_type else ''
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

def save_keyframes(keyframes, keyframe_indices, save_dir, prefix, logger):
    os.makedirs(save_dir, exist_ok=True)
    for i, (frame, idx) in enumerate(zip(keyframes, keyframe_indices)):
        path = os.path.join(save_dir, f'{prefix}_keyframe_{i+1:03d}_frame{idx:06d}.png')
        cv2.imwrite(path, frame)
    logger.info(f'  Keyframes saved to: {save_dir} ({len(keyframes)} files)')


def main(video, screenshots, utg, logger, keyframes_dir=None, keyframes_prefix='keyframe'):
    total_start = time.time()

    # ------------------------------------------------------------------
    # Step 1: Keyframe location
    # ------------------------------------------------------------------
    logger.info('=' * 50)
    logger.info('STEP 1: Keyframe Location')
    logger.info(f'  Input video : {video}')
    step_start = time.time()

    keyframe_sequence, keyframe_index = keyframe_location(video)

    elapsed = time.time() - step_start
    logger.info(f'  Keyframes found   : {len(keyframe_index)}')
    logger.info(f'  Keyframe indices  : {keyframe_index}')
    logger.info(f'  Duration          : {elapsed:.2f}s')

    # ------------------------------------------------------------------
    # Save keyframes to disk
    # ------------------------------------------------------------------
    if keyframes_dir is not None:
        save_keyframes(keyframe_sequence, keyframe_index, keyframes_dir, keyframes_prefix, logger)

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

    store_trace(utg, traces, args.out, logger)

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

    if args.log_dir:
        log_dir = args.log_dir
    else:
        log_dir = os.path.dirname(os.path.dirname(os.path.abspath(args.out)))

    video_basename = os.path.basename(args.video) if args.video else ''
    if 'hhv' in video_basename:
        video_type = 'hhv'
    elif 'srv' in video_basename:
        video_type = 'srv'
    else:
        video_type = ''

    logger = setup_logger(log_dir, video_type)

    keyframes_dir = args.save_keyframes if args.save_keyframes else \
        os.path.join(os.path.dirname(os.path.abspath(args.out)), 'keyframes')

    # e.g. "utg01_hhv" derived from the utg directory name and video type
    utg_dirname = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(args.utg))))
    keyframes_prefix = f'{utg_dirname}_{video_type}' if video_type else utg_dirname

    logger.info('GIFdroid started')
    logger.info(f'  --video          : {args.video}')
    logger.info(f'  --utg            : {args.utg}')
    logger.info(f'  --artifact       : {args.artifact}')
    logger.info(f'  --out            : {args.out}')
    logger.info(f'  --log-dir        : {args.log_dir}')
    logger.info(f'  --save-keyframes : {keyframes_dir}')

    if args.video is None or args.utg is None or args.artifact is None:
        logger.error('Missing required arguments. Run with -h for usage.')
        exit(1)

    # Idempotency check: skip if the output trace already exists
    if os.path.isfile(args.out):
        logger.info(f'Output already exists, skipping: {args.out}')
        exit(0)

    main(args.video, args.artifact, args.utg, logger, keyframes_dir=keyframes_dir, keyframes_prefix=keyframes_prefix)
