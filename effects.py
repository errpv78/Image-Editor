import cv2
import imutils
import numpy as np
from resize_image import resize_image
from matplotlib import pyplot as plt
from time import sleep

def to_gray(image,print_state=True):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if print_state:
        cv2.imshow("Press any key to continue",gray)
        l = cv2.waitKey(0)
        if l:
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
    return gray

def to_blue(image,print_state=True):
    blue = cv2.cvtColor(image, cv2.IMREAD_ANYCOLOR)
    if print_state:
        cv2.imshow("Press any key to continue", blue)
        l = cv2.waitKey(0)
        if l:
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
    return blue

def blur(image,mode=0,print_state=True):
    if mode==0:
        blur = cv2.GaussianBlur(image, (3,3),0)
    else:
        blur = cv2.GaussianBlur(image, (5,5),0)
    if print_state:
        cv2.imshow("Press any key to continue", blur)
        l = cv2.waitKey(0)
        if l:
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()

    return blur

def edges(image,print_state=True):
    edge = cv2.Canny(image, 100,200)
    if print_state:
        cv2.imshow("Press any key to continue", edge)
        l = cv2.waitKey(0)
        if l:
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
    return edge

# image = cv2.imread("virat.jpeg")
# # image = resize_image(image)
# edges(image,True)