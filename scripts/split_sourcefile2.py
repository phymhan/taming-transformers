import os
import random

random.seed(0)

# src = '/nfs/lhan/data/moving_shapes/shapes_v2_staticbg/file_list.txt'
# out1 = '/nfs/lhan/data/moving_shapes/shapes_v2_staticbg/train_list.txt'
# out2 = '/nfs/lhan/data/moving_shapes/shapes_v2_staticbg/val_list.txt'
# src = '/nfs/lhan/data/vox-celeba-alex-train/vox+celeb+sketch+mask.txt'
# out1 = '/nfs/lhan/data/vox-celeba-alex-train/vox+celeb+sketch+mask_train.txt'
# out2 = '/nfs/lhan/data/vox-celeba-alex-train/vox+celeb+sketch+mask_val.txt'
# src = '/nfs/lhan/data/vox-celeba-alex-train/vox30k+all.txt'
# out1 = '/nfs/lhan/data/vox-celeba-alex-train/vox30k+all_train.txt'
# out2 = '/nfs/lhan/data/vox-celeba-alex-train/vox30k+all_val.txt'
# src = '/nfs/lhan/data/DALLE/shapes_v2/video+visual.txt'
# out1 = '/nfs/lhan/data/DALLE/shapes_v2/video+visual_train.txt'
# out2 = '/nfs/lhan/data/DALLE/shapes_v2/video+visual_val.txt'



# src = '/nfs/lhan/data/vox-celeba-alex-train/mask_v0+draw_v0.txt'
# out1 = '/nfs/lhan/data/vox-celeba-alex-train/mask_v0+draw_v0_train.txt'
# out2 = '/nfs/lhan/data/vox-celeba-alex-train/mask_v0+draw_v0_val.txt'

# src = '/nfs/lhan/data/vb100/data/video_list.txt'
# out1 = '/nfs/lhan/data/vb100/data/video_list_train.txt'
# out2 = '/nfs/lhan/data/vb100/data/video_list_val.txt'

# nval = 10

# with open(src, 'r') as f:
#     all_files = f.readlines()

# random.shuffle(all_files)

# with open(out1, 'w') as f:
#     f.write(''.join(all_files[nval:]))

# with open(out2, 'w') as f:
#     f.write(''.join(all_files[:nval]))



# src1 = '/nfs/lhan/data/vb100/mask_crop_list.txt'
# src2 = '/nfs/lhan/data/vb100/frame_crop_list.txt'
# out1 = '/nfs/lhan/data/vb100/mask+frame_train.txt'
# out2 = '/nfs/lhan/data/vb100/mask+frame_val.txt'

src1 = '/nfs/lhan/data/DALLE/multi-bird/cub200.txt'
src2 = '/nfs/lhan/data/vb100/frame_crop_list.txt'
out1 = '/nfs/lhan/data/DALLE/multi-bird/cub200+vb100_train.txt'
out2 = '/nfs/lhan/data/DALLE/multi-bird/cub200+vb100_val.txt'

nval = 1000

with open(src1, 'r') as f:
    all_files1 = f.readlines()

with open(src2, 'r') as f:
    all_files2 = f.readlines()
random.shuffle(all_files2)
all_files2 = all_files2[:len(all_files1)*5]

all_files = all_files1 + all_files2

all_files = [s.rstrip() for s in all_files]

random.shuffle(all_files)

with open(out1, 'w') as f:
    f.write('\n'.join(all_files[nval:]))

with open(out2, 'w') as f:
    f.write('\n'.join(all_files[:nval]))