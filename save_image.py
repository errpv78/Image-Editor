import cv2
import imutils

def save_img(image_name,image):
    action = input("Do you want to overwrite original image(y/n): ")
    if action=='y':
        new_name = image_name
        cv2.imwrite(new_name,image)
    else:
        new_name = "new_"+image_name
        cv2.imwrite(new_name, image)
    print("Image saved as",new_name)