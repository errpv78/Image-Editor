from torchvision import models
import torch
import cv2
from torchvision import transforms
from PIL import Image
from resizeimage import resizeimage
import numpy as np

transform = transforms.Compose([transforms.Resize(256),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize( mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
                                ])
# import os
# os.environ['TORCH_HOME'] = '/home/err_pv/Desktop/Parikh_linux/Deep Learning/openCV/Image-Editor' #setting the environment variable
wide_resnet = models.wide_resnet50_2(pretrained=True, progress=True)

with open("trip1.jpg", 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [ 600, 400])
image = cover
# # Convert RGB to BGR
# image = image[:, :, ::-1].copy()
# cv2.imshow("Press any key to continue", image)
# l = cv2.waitKey(0)
image.show()

import json
class_idx = json.load(open("imagenet_class_index.json"))
# print(class_idx)
idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]

transformed_image = transform(image)
batch = torch.unsqueeze(transformed_image, 0)
wide_resnet.eval()
output = wide_resnet(batch)

for idx in output[0].sort()[1][-1:]:
    print(idx2label[idx])