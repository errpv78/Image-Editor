import cv2
import imutils
import numpy as np
from resize_image import resize_image
from matplotlib import pyplot as plt
from time import sleep

def to_gray(image,print_state=True):
    i = -1
    l = 0
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    shade = gray
    while l!=13:
        if l==82:
            if i<15:
                i+=1
        elif l==84:
            if i>-1:
                i-=1
        if i==-1:
            shade = image
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==0:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)
        elif i==1:
            ret, shade = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)
        elif i==2:
            ret, shade = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)
        elif i==3:
            ret, shade = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)
        elif i==4:
            ret, shade = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)
        elif i==5:
            ret, shade = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)
        elif i==6:
            ret, shade = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)
        elif i==7:
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            ret, shade = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            cv2.imshow("Press enter key to continue, up-down to change shade",shade)
            l = cv2.waitKey(0)

        elif i==8:
            shade = cv2.cvtColor(image, cv2.IMREAD_ANYCOLOR)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==9:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==10:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==11:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==12:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==13:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==14:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)
        elif i==15:
            shade = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
            cv2.imshow("Press enter key to continue, up-down to change shade", shade)
            l = cv2.waitKey(0)

    gray = shade
    cv2.destroyAllWindows()
    return gray


def blur(image,print_state=True):
    i = 0
    l = -1
    temp = image
    blur = image
    while l!=13:
        if l==82:
            if i<4:
                i+=1
        elif l==84:
            if i>0:
                i-=1
        if l==-1:
            blur = temp
            cv2.imshow("Press enter key to continue, up-down to change blur", blur)
            l = cv2.waitKey(0)
        if i==0:
            blur = temp
            cv2.imshow("Press enter key to continue, up-down to change blur", blur)
            l = cv2.waitKey(0)
        elif i==1:
            kernel = np.ones((5, 5), np.float32) / 25
            blur = cv2.filter2D(temp,-1, kernel)
            cv2.imshow("Press enter key to continue, up-down to change blur", blur)
            l = cv2.waitKey(0)
        elif i==2:
            blur = cv2.GaussianBlur(temp,(5,5),0)
            cv2.imshow("Press enter key to continue, up-down to change blur", blur)
            l = cv2.waitKey(0)
        elif i==3:
            blur = cv2.medianBlur(temp,5)
            cv2.imshow("Press enter key to continue, up-down to change blur", blur)
            l = cv2.waitKey(0)
        elif i==4:
            blur = cv2.bilateralFilter(temp,9,75,75)
            cv2.imshow("Press enter key to continue, up-down to change blur", blur)
            l = cv2.waitKey(0)
        else:
            break
    final = blur
    cv2.destroyAllWindows()
    return final

def edges(image,print_state=True):
    minVal = 50
    maxVal = 100
    edge = image
    l = -1
    while l!=13:
        if l==82:
            if minVal+5<=maxVal:
                minVal+=5
        elif l==84:
            if minVal-5>=0:
                minVal-=5
        elif l==83:
            if maxVal+5<=255:
                maxVal+=5
        elif l==81:
            if maxVal-5 > minVal:
                maxVal-=5
        edge = cv2.Canny(image, minVal, maxVal)
        cv2.imshow("Press arrow key to adjust edges, enter to continue", edge)
        l = cv2.waitKey(0)
    cv2.destroyAllWindows()
    return edge

# image = cv2.imread("virat.jpeg")
# # # image = resize_image(image)
# edges(image,True)