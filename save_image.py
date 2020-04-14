import cv2
import imutils

def save_img(image_name,image,new_image):
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.imshow("Edited Image", new_image)
    cv2.waitKey(0)

    action = input("Do you want to overwrite original image(y/n) or save as new image: ")
    if action == 'y':
        cv2.imwrite(image_name, new_image)
        print("Image saved as", image_name)
    else:
        new_name = "new_" + image_name
        cv2.imwrite(new_name, image)
        print("Image saved as", new_name)
