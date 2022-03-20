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

# src = '/nfs/lhan/data/vb100/frame_crop_list.txt'
# out1 = '/nfs/lhan/data/vb100/frame_crop_list_train.txt'
# out2 = '/nfs/lhan/data/vb100/frame_crop_list_val.txt'

# src = '/dresden/users/lh599/Data/iPER/frames_all.txt'
# out1 = '/dresden/users/lh599/Data/iPER/frames_train.txt'
# out2 = '/dresden/users/lh599/Data/iPER/frames_val.txt'

# src = '/dresden/users/lh599/Active/muri-scan/lezi_cropped_all.txt'
# out1 = '/dresden/users/lh599/Active/muri-scan/lezi_cropped_train.txt'
# out2 = '/dresden/users/lh599/Active/muri-scan/lezi_cropped_val.txt'

src = '/dresden/users/lh599/Data/kinetics-dataset/six_god_list2.txt'
out1 = '/dresden/users/lh599/Data/kinetics-dataset/six_god_list_train2.txt'
out2 = '/dresden/users/lh599/Data/kinetics-dataset/six_god_list_val2.txt'

nval = 1000

with open(src, 'r') as f:
    all_files = f.readlines()

all_files = ['/dresden/users/lh599/Data/kinetics-dataset/k400_parts/'+s for s in all_files]

random.shuffle(all_files)

# with open(out1, 'w') as f:
#     f.write(''.join(all_files[nval:]))

# with open(out2, 'w') as f:
#     f.write(''.join(all_files[:nval]))

with open(out1, 'w') as f:
    f.write(''.join(all_files[nval:]))

with open(out2, 'w') as f:
    f.write(''.join(all_files[:nval]))



# src1 = '/nfs/lhan/data/vox-celeba-alex-train/mask_v0+draw_v0.txt'
# src2 = '/nfs/lhan/data/vox-celeba-alex-train/vox-celeba-alex-train.txt'
# out1 = '/nfs/lhan/data/vox-celeba-alex-train/mask_v0+draw_v0+vox_train.txt'
# out2 = '/nfs/lhan/data/vox-celeba-alex-train/mask_v0+draw_v0+vox_val.txt'

# nval = 5000

# with open(src1, 'r') as f:
#     all_files1 = f.readlines()

# with open(src2, 'r') as f:
#     all_files2 = f.readlines()
# random.shuffle(all_files2)
# all_files2 = all_files2[:len(all_files1)]

# all_files = all_files1 + all_files2

# all_files = [s.rstrip() for s in all_files]

# random.shuffle(all_files)

# with open(out1, 'w') as f:
#     f.write('\n'.join(all_files[nval:]))

# with open(out2, 'w') as f:
#     f.write('\n'.join(all_files[:nval]))