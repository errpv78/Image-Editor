import cv2
import imutils
import numpy as np
from save_image import save_img
from resizeimage import resizeimage
from PIL import Image


def resize_image(image):
    resize_choice = int(input("Enter choice: 1. Manual Crop 2. Aspect Ratio Intact 3.Exit\n"))
    (h, w, d) = image.shape
    if resize_choice==1:
        done = 0
        while not(done):
            height = int(input("Enter new height: "))
            width = int(input("Enter new width: "))
            dim = [min(w, width) , min(h, height)]
            temp_image = image[:, :, ::-1].copy()
            temp_image = Image.fromarray(temp_image)
            resized = resizeimage.resize_cover(temp_image, dim)
            resized = np.array(resized)
            # Convert RGB to BGR
            resized = resized[:, :, ::-1].copy()
            print("Loading Image..")
            cv2.imshow("If satisfied press 1 else 0", resized)
            done = cv2.waitKey(0)
            # print(done)
            if done==49:
                cv2.destroyAllWindows()
                break
            else:
                cv2.destroyAllWindows()
                done=0

    elif resize_choice==2:
        done = 0
        while not(done):
            new_h = int(input("Enter height: "))
            r = new_h / h
            dim = [min(w, int(r*w)),min(h, new_h)]
            temp_image = image[:, :, ::-1].copy()
            temp_image = Image.fromarray(temp_image)
            resized = resizeimage.resize_cover(temp_image, dim)
            resized = np.array(resized)
            # Convert RGB to BGR
            resized = resized[:, :, ::-1].copy()
            print("Loading Image..")
            cv2.imshow("If satisfied press 1 else 0", resized)
            done = cv2.waitKey(0)
            # print(done)
            if done == 49:
                cv2.destroyAllWindows()
                break
            else:
                cv2.destroyAllWindows()
                done = 0
    else:
        return image
    return resized


# resize_image("nature.jpeg")