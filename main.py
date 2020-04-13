import imutils
import cv2
print("Welcome to awesome image editor!!\n")
print("*****MENU****")
print("1. Resize Image")

image_name = input("Enter image name (with extension): ")

choice = int(input("Enter choice: "))

if choice==1:

    resize_image(image_name)

