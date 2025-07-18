import os
import shutil
import random
import numpy as np
from pathlib import Path
import scipy.io
from tqdm import tqdm

# ==============================================================================
DATASET_ROOT = Path('./YOLO-Training/Penn_Action')
IMG_WIDTH = 640
IMG_HEIGHT = 480

LABELS_MAT_DIR = DATASET_ROOT / "labels"
FRAMES_DIR = DATASET_ROOT / "frames"
OUTPUT_ROOT = DATASET_ROOT / "dataset"

TRAIN_RATIO = 0.8  # 80/20
# ==============================================================================

def create_dir(path):
    path.mkdir(parents=True, exist_ok=True)

def safe_scalar(val):
    """Convert single-value arrays to scalar, handle NaNs"""
    if isinstance(val, np.ndarray):
        val = val.flatten()[0]
    if np.isnan(val):
        return 0.0
    return float(val)

def convert_penn_to_yolo_and_split():
    if not LABELS_MAT_DIR.is_dir() or not FRAMES_DIR.is_dir():
        print("labels or frames folder missing!")
        return

    mat_files = sorted(list(LABELS_MAT_DIR.glob("*.mat")))
    print(f"Found {len(mat_files)} annotation files.")

    # Split into train/val by sequence
    random.shuffle(mat_files)
    split_idx = int(len(mat_files) * TRAIN_RATIO)
    train_files = mat_files[:split_idx]
    val_files = mat_files[split_idx:]

    print(f"Splitting into {len(train_files)} train and {len(val_files)} val sequences.")

    for split in ['train', 'val']:
        create_dir(OUTPUT_ROOT / f'images/{split}')
        create_dir(OUTPUT_ROOT / f'labels/{split}')

    # Process each split
    for split, files in [('train', train_files), ('val', val_files)]:
        for mat_file in tqdm(files, desc=f"Processing {split}"):
            seq_id = mat_file.stem  # e.g., '0001'
            data = scipy.io.loadmat(mat_file)

            bboxes = data['bbox']
            keypoints_x = data['x']
            keypoints_y = data['y']
            visibility = data['visibility']

            nframes = min(bboxes.shape[0], keypoints_x.shape[0], keypoints_y.shape[0], visibility.shape[0])

            for frame_idx in range(nframes):
                try:
                    x_min = safe_scalar(bboxes[frame_idx][0])
                    y_min = safe_scalar(bboxes[frame_idx][1])
                    x_max = safe_scalar(bboxes[frame_idx][2])
                    y_max = safe_scalar(bboxes[frame_idx][3])

                    x_center = (x_min + x_max) / 2 / IMG_WIDTH
                    y_center = (y_min + y_max) / 2 / IMG_HEIGHT
                    width = (x_max - x_min) / IMG_WIDTH
                    height = (y_max - y_min) / IMG_HEIGHT

                    frame_kpts_x = keypoints_x[frame_idx].flatten()
                    frame_kpts_y = keypoints_y[frame_idx].flatten()
                    frame_vis = visibility[frame_idx].flatten()

                    yolo_keypoints = []
                    for kpt_idx in range(len(frame_kpts_x)):
                        kpt_x_norm = safe_scalar(frame_kpts_x[kpt_idx]) / IMG_WIDTH
                        kpt_y_norm = safe_scalar(frame_kpts_y[kpt_idx]) / IMG_HEIGHT
                        yolo_visibility = int(safe_scalar(frame_vis[kpt_idx])) + 1
                        yolo_keypoints.extend([kpt_x_norm, kpt_y_norm, yolo_visibility])

                    kpts_str = " ".join(f"{v:.6f}" for v in yolo_keypoints)
                    yolo_line = f"0 {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f} {kpts_str}"

                    # Output filename keeps seq_id and frame number
                    output_label = OUTPUT_ROOT / f'labels/{split}/{seq_id}_{frame_idx+1:06d}.txt'
                    output_label.write_text(yolo_line)

                    # Copy frame image: /frames/{seq_id}/{frame_idx+1:06d}.jpg
                    src_img = FRAMES_DIR / seq_id / f"{frame_idx+1:06d}.jpg"
                    if src_img.is_file():
                        dst_img = OUTPUT_ROOT / f'images/{split}/{seq_id}_{frame_idx+1:06d}.jpg'
                        shutil.copy(src_img, dst_img)
                    else:
                        print(f"Missing image: {src_img}")

                except Exception as e:
                    print(f"Error at seq {seq_id} frame {frame_idx+1}: {e}")

    print("\nAll done! Labels & images saved under:")
    print(f"{OUTPUT_ROOT.resolve()}")

if __name__ == '__main__':
    random.seed(42)
    convert_penn_to_yolo_and_split()
