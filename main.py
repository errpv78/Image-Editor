import imutils
import cv2
import pathlib
from resize_image import resize_image
from effects import to_blue,blur,to_gray,edges
from rotate_image import rotate
from save_image import save_img

print("Welcome to awesome image editor!!\n")
load = False

print("Load Image..")
image = None
while image is None:
    image_name=input("Enter image name(with extension): ")
    image = cv2.imread(image_name)
    if image is None:
        print("Image not found")
    else:
        (h, w, d) = image.shape
        r = 300 / h
        dim = (int(r * w), 300)
        image = cv2.resize(image, dim)
        cv2.imshow("Press any key to continue",image)
        l = cv2.waitKey(0)
        if l:
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
original = image

while True:
    menu = "*****MENU*****"
    print(menu.center(40))
    l = ["1. Resize image", "2. Blur image", "3. Blue-effect" ,"4. Gray-effect" ,"5. Rotate image", "6. Image-edges", "20. Save image", "0. Exit"]
    for i in l:
        print(i)
    choice = int(input("Enter choice: "))

    if choice==0:
        opt = input("Do you want to save changes(y/n): ")
        if opt=='y':
            save_img(image_name, image, new)
        print("Thank you!\nExiting..")
        break
    elif choice==1:
        new = resize_image(image)
    elif choice==2:
        mode = int(input("Enter blur mode (high 1/low 0): "))
        new = blur(image,blur)
    elif choice==3:
        new = to_blue(image)
    elif choice==4:
        new = to_gray(image)
    elif choice==5:
        new = rotate(image)
    elif choice==6:
        new = edges(image)
    elif choice==20:
        save_img(image_name, image, new)
    else:
        print("Invalid Choice")

    if choice in range(7):
        s = int(input("To save changes press 1, to discard changes press 0: "))
        if s==1:
            image = new