import cv2
import imutils

def save_img(image_name,image,new_image):
    cv2.imshow("Original Image Press any ley to continue", image)
    l = cv2.waitKey(0)
    if l:
        cv2.destroyAllWindows()
    else:
        cv2.destroyAllWindows()
    cv2.imshow("Edited Image, press any key to continue", new_image)
    l = cv2.waitKey(0)
    if l:
        cv2.destroyAllWindows()
    else:
        cv2.destroyAllWindows()

    action = input("Do you want to overwrite original image(y/n) or save as new image: ")
    if action == 'y':
        cv2.imwrite(image_name, new_image)
        print("Image saved as", image_name)
    else:
        new = input("Enter new name: ")
        new_name = new + image_name
        cv2.imwrite(new_name, image)
        print("Image saved as", new_name)
