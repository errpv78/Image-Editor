import cv2
import imutils

def rotate(image):
    type = int(input("Chose: 1. Fixed Rotate 2. Variable Rotate \n"))
    if type==1:
        done=0
        rotated = image
        while not(done):
            dirn = input("Chose direction (r/l): ")
            if dirn=='r':
                rotated = imutils.rotate_bound(rotated, 90)
                print("Image loading, if satisfied press 1 else press 0")
                cv2.imshow("Rotated", rotated)
                done = cv2.waitKey(0)
            else:
                rotated = imutils.rotate_bound(rotated, -90)
                print("Image loading, if satisfied press 1 else press 0")
                cv2.imshow("Imutils Bound Rotation", rotated)
                done = cv2.waitKey(0)
            if done==49:
                cv2.destroyAllWindows()
                break
            else:
                cv2.destroyAllWindows()
                done=0

    else:
        done = 0
        while not (done):
            degree = int(input("Enter degrees to rotate: "))
            rotated = imutils.rotate_bound(image, degree)
            print("Image loading, if satisfied press 1 else press 0")
            cv2.imshow("Rotated", rotated)
            done = cv2.waitKey(0)
            if done == 49:
                cv2.destroyAllWindows()
                break
            else:
                cv2.destroyAllWindows()
                done = 0
    return rotated

# image = cv2.imread("nature.jpeg")
# rotate(image)