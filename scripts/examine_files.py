
import bisect
import numpy as np
import albumentations
from PIL import Image
from torch.utils.data import Dataset, ConcatDataset

import pdb
st = pdb.set_trace

import os
from tqdm import tqdm
from random import randint

class ImagePaths(Dataset):
    def __init__(self, paths, size=None, random_crop=False, labels=None):
        self.size = size
        self.random_crop = random_crop

        self.labels = dict() if labels is None else labels
        self.labels["file_path_"] = paths
        self._length = len(paths)

        if self.size is not None and self.size > 0:
            self.rescaler = albumentations.SmallestMaxSize(max_size = self.size)
            if not self.random_crop:
                self.cropper = albumentations.CenterCrop(height=self.size,width=self.size)
            else:
                self.cropper = albumentations.RandomCrop(height=self.size,width=self.size)
            self.preprocessor = albumentations.Compose([self.rescaler, self.cropper])
        else:
            self.preprocessor = lambda **kwargs: kwargs

    def __len__(self):
        return self._length

    def preprocess_image(self, image_path):
        image = Image.open(image_path)
        if not image.mode == "RGB":
            image = image.convert("RGB")
        try:
            image = np.array(image).astype(np.uint8)
        except:
            print(f"Skipping file {image_path}")
            print(f"mv {image_path} {image_path}.broken")
            os.system(f"mv {image_path} {image_path}.broken")
            return None
        image = self.preprocessor(image=image)["image"]
        image = (image/127.5 - 1.0).astype(np.float32)
        return image
    
    def random_sample(self):
        return self.__getitem__(randint(0, self.__len__() - 1))
    
    def skip_sample(self, ind):
        return self.random_sample()
    
    def __getitem__(self, i):
        example = dict()
        image = self.preprocess_image(self.labels["file_path_"][i])
        if image is None:
            return self.skip_sample(i)
        example["image"] = image
        for k in self.labels:
            example[k] = self.labels[k][i]
        return example


with open('/nfs/lhan/data/MUG/155.207.19.233/all_imgs.txt', 'r') as f:
    paths = [p.rstrip() for p in f.readlines()]
image_processor = ImagePaths(paths, 128)

for i in tqdm(range(39233, len(image_processor))):
    # print(paths[i])
    image_processor.__getitem__(i)
