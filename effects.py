import cv2
import imutils
import numpy as np
from resize_image import resize_image
from matplotlib import pyplot as plt
from time import sleep

def to_gray(image,print_state=False):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if print_state:
        cv2.imshow("Gray",gray)
        cv2.waitKey(0)
    return gray

def to_blue(image,print_state=False):
    blue = cv2.cvtColor(image, cv2.IMREAD_ANYCOLOR)
    if print_state:
        cv2.imshow("Blue-effect", blue)
        cv2.waitKey(0)
    return blue

def blur(image,mode=0,print_state=False):
    if mode==0:
        blur = cv2.GaussianBlur(image, (3,3),0)
    else:
        blur = cv2.GaussianBlur(image, (5,5),0)
    if print_state:
        cv2.imshow("Blurred", blur)
        cv2.waitKey(0)

    return blur

def edges(image,print_state=False):
    edge = cv2.Canny(image, 100,200)
    if print_state:
        cv2.imshow("Edges", edge)
        cv2.waitKey(0)
    return edge

# image = cv2.imread("virat.jpeg")
# # image = resize_image(image)
# edges(image,True)