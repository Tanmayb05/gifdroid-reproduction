from skimage.metrics import structural_similarity as ssim
import cv2
import glob
import logging
import os
import time
import matplotlib.pyplot as plt

logger = logging.getLogger('src_gifdroid.mapping')


def load_screenshots(screenshots):
    """Load all artifact PNGs, extract ORB descriptors and grayscale images for matching."""
    t0 = time.time()
    index = {}
    size = None
    orb = cv2.ORB_create(nfeatures=1500)
    for imagePath in glob.glob(os.path.join(screenshots, '*.png')):
        filename = imagePath[imagePath.rfind("/") + 1:]
        stem = filename.replace('artifacts_', '').replace('.png', '')
        if not stem.isdigit():
            continue
        image = cv2.imread(imagePath)
        size = image.shape
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, des = orb.detectAndCompute(image, None)
        index[filename] = {'ssim': image, 'orb': des, 'size': image.shape}
    elapsed = time.time() - t0
    logger.debug(f'load_screenshots: {len(index)} screenshots loaded in {elapsed:.2f}s from "{screenshots}"')
    return index, size


def match_bfmatcher(des1, des2):
    """Compute ratio-test ORB match score between two descriptor sets (0.0–1.0)."""
    if des1 is None or des2 is None:
        return 0.0
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(des1, des2, k=2)
    if len(matches) == 0:
        return 0.0
    good = []
    for pair in matches:
        if len(pair) == 2:
            m, n = pair
            # Lowe's ratio test: keep match only if significantly better than second-best
            if m.distance < 0.4 * n.distance:
                good.append([m])
    return len(good) / len(matches)


def mapping(image, index, size):
    """
    Match a keyframe image against the screenshot index.
    Score = 0.5 * SSIM + 0.5 * ORB ratio-test score.
    Returns the filename of the best-matching artifact screenshot.
    """
    alpha = 0.5
    orb = cv2.ORB_create(nfeatures=1500)
    results = {}
    image = cv2.resize(image, (size[1], size[0]))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, des = orb.detectAndCompute(image_gray, None)
    for (k, v) in index.items():
        scr_h, scr_w = v['size']
        kf_resized = cv2.resize(image_gray, (scr_w, scr_h))
        sim_ssim = ssim(kf_resized, v['ssim'])
        sim_orb = match_bfmatcher(des, v['orb'])
        results[k] = alpha * sim_ssim + (1 - alpha) * sim_orb
    results = sorted([(v, k) for (k, v) in results.items()], reverse=True)
    best = results[0][1]
    logger.debug(f'mapping: best match "{best}" (score={results[0][0]:.3f})')
    return best


def mapping_with_scores(image, index, size):
    """
    Same as mapping() but returns the full ranked score list for robustness analysis.
    Returns: (best_match_filename, sorted_scores)
      sorted_scores: list of (score, filename) sorted descending
    """
    alpha = 0.5
    orb = cv2.ORB_create(nfeatures=1500)
    results = {}
    image = cv2.resize(image, (size[1], size[0]))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, des = orb.detectAndCompute(image_gray, None)
    for (k, v) in index.items():
        scr_h, scr_w = v['size']
        kf_resized = cv2.resize(image_gray, (scr_w, scr_h))
        sim_ssim = ssim(kf_resized, v['ssim'])
        sim_orb = match_bfmatcher(des, v['orb'])
        results[k] = alpha * sim_ssim + (1 - alpha) * sim_orb
    sorted_results = sorted([(v, k) for (k, v) in results.items()], reverse=True)
    best = sorted_results[0][1]
    logger.debug(f'mapping_with_scores: best match "{best}" (score={sorted_results[0][0]:.3f})')
    return best, sorted_results


def gui_mapping(screenshots, keyframes):
    """
    Map each keyframe to its closest artifact screenshot.
    Returns a list of integer screen IDs corresponding to the keyframe sequence.
    """
    t0 = time.time()
    logger.info(f'gui_mapping: matching {len(keyframes)} keyframes against screenshots in "{screenshots}"')

    index, size = load_screenshots(screenshots)
    index_sequence = [mapping(keyframe, index, size) for keyframe in keyframes]
    index_sequence = [int(i.split('artifacts_')[1].split('.')[0]) for i in index_sequence]

    elapsed = time.time() - t0
    logger.info(f'gui_mapping: done — index sequence {index_sequence} ({elapsed:.2f}s)')
    return index_sequence

if __name__ == "__main__":
    # Debug
    index, size = load_screenshots('/Users/mac/Documents/Python/DroidbotMapping/dataset/firebase/KISS/artifacts')
    frame_id = 11
    vidcap = cv2.VideoCapture('/Users/mac/Documents/Python/DroidbotMapping/dataset/GT/KISS/2.gif')
    success, frame = vidcap.read()
    no = 1
    while success: 
        success, frame = vidcap.read()  
        if not success:
            break
        no += 1
        if no == frame_id:
            keyframe = frame
            break
    vidcap.release()
    print('Start Mapping')
    print(mapping(keyframe, index, size))
