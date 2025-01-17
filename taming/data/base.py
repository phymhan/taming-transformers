import bisect
import numpy as np
import albumentations
from PIL import Image
from torch.utils.data import Dataset, ConcatDataset
from random import randint
import decord
decord.bridge.set_bridge("torch")
import random
import pdb
st = pdb.set_trace

class ConcatDatasetWithIndex(ConcatDataset):
    """Modified from original pytorch code to return dataset idx"""
    def __getitem__(self, idx):
        if idx < 0:
            if -idx > len(self):
                raise ValueError("absolute value of index should not exceed dataset length")
            idx = len(self) + idx
        dataset_idx = bisect.bisect_right(self.cumulative_sizes, idx)
        if dataset_idx == 0:
            sample_idx = idx
        else:
            sample_idx = idx - self.cumulative_sizes[dataset_idx - 1]
        return self.datasets[dataset_idx][sample_idx], dataset_idx


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


class NumpyPaths(ImagePaths):
    def preprocess_image(self, image_path):
        image = np.load(image_path).squeeze(0)  # 3 x 1024 x 1024
        image = np.transpose(image, (1,2,0))
        image = Image.fromarray(image, mode="RGB")
        image = np.array(image).astype(np.uint8)
        image = self.preprocessor(image=image)["image"]
        image = (image/127.5 - 1.0).astype(np.float32)
        return image


class VideoPaths(Dataset):
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
        try:
            video_reader = decord.VideoReader(image_path, num_threads=1)
            idx = random.randint(0, len(video_reader) - 1)
            image = video_reader.get_batch([idx])
        except:
            print(f"Skipping file {image_path}")
            return None
        image = image.numpy().squeeze()
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


class ImageStackPaths(Dataset):
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
        try:
            imgs = Image.open(image_path).convert('RGB')  # size (W, H)
            imgs = np.array(imgs)  # shape (H, W, C)
            horizontal = imgs.shape[1] > imgs.shape[0]
            shorter, longer = min(imgs.shape[0], imgs.shape[1]), max(imgs.shape[0], imgs.shape[1])
            vlen = longer // shorter
            frames = np.split(imgs, vlen, axis=1 if horizontal else 0)
            idx = random.randint(0, vlen - 1)
            image = frames[idx]
        except:
            print(f"Skipping file {image_path}")
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
