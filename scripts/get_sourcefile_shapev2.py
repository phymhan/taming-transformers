import os
import random
from natsort import natsorted
import numpy as np
from tqdm import tqdm

import pdb
st = pdb.set_trace

random.seed(0)
np.random.seed(0)

nvids = 30000

src = '/nfs/lhan/data/DALLE/shapes_v2/visual'

# vids = np.random.choice(os.listdir(src))
vids = os.listdir(src)
# random.shuffle(vids)
# vids = vids[:nvids]

# with open(f'/nfs/lhan/data/vox-celeba-alex-train/vids_{nvids}.txt', 'w') as f:
#     f.write('\n'.join(vids)+'\n')

frame_num = 4
frame_step = 1
imgs = []

for vid in tqdm(vids):
    frames = natsorted(os.listdir(os.path.join(src, vid)))
    video_len = len(frames)
    start_idx = random.randint(0, video_len - (frame_num - 1) * frame_step - 1)
    for j in range(start_idx, start_idx+frame_num*frame_step, frame_step):
        imgs.append(os.path.join(src, vid, frames[j]))

with open(f'/nfs/lhan/data/DALLE/shapes_v2/visual_{nvids}x{frame_num}.txt', 'w') as f:
    f.write('\n'.join(imgs)+'\n')
