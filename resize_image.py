import cv2
import imutils
import numpy as np
from save_image import save_img

def resize_image(image):
    resize_choice = int(input("Enter choice: 1. Manual Crop 2. Aspect Ratio Intact 3.Exit\n"))
    if resize_choice==1:
        done = 0
        while not(done):
            height = int(input("Enter height: "))
            width = int(input("Enter width: "))
            dim = (width, height)
            resized = cv2.resize(image,dim)
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
        (h, w, d) = image.shape

        done = 0

        while not(done):
            new_h = int(input("Enter height: "))
            r = new_h / h
            dim = (int(r*w),new_h)
            resized = cv2.resize(image, dim)
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