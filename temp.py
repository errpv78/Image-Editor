import os

os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,30).__str__()
import cv2 # import after setting OPENCV_IO_MAX_IMAGE_PIXELS

image = cv2.imread("trip1.jpg")
cv2.imshow("image",image)
cv2.waitKey(0)

i1 = cv2.resize(image,(500,300))
cv2.imshow("older",i1)
cv2.waitKey(0)

i2 = cv2.resize(image,(500,300), interpolation = cv2.INTER_CUBIC)
cv2.imshow("new",i2)
cv2.waitKey(0)