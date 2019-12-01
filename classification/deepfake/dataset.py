import torch
from PIL import Image
import json
import numpy as np
import torchvision.transforms as transforms
import os
identity = lambda x:x

class SimpleDataset:
    def __init__(self, data_file, transform, target_transform=identity):
        with open(data_file, 'r') as f:
            self.meta = json.load(f)
        self.transform = transform
        self.target_transform = target_transform
        

    def __getitem__(self,i):
        # image_path = os.path.join(self.meta['image_names'][i])
        image_path = self.meta['names'][i]
        img = Image.open(image_path).convert('RGB')
        img = self.transform(img)
        target = self.target_transform(self.meta['labels'][i])
        return img, target

    def __len__(self):
        return len(self.meta['names'])
