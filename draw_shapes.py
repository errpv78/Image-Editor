import cv2
import numpy as np

def shape(image):
    (h,w,d) = image.shape
    temp = image
    choice = input("Enter Shape (1 Rectangle, 2 Circle): ")
    choice = int(choice)
    x1,y1 = w//2-20,h//2-20
    x2,y2 = w//2+20,h//2+20
    if choice==1:
        l = -1
        while l!=49:
            temp1 = temp.copy()
            if l==-1:
                cv2.rectangle(temp1,(x1,y1),(x2,y2),2 )
                cv2.imshow("rectangle", temp1)
                l = cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif l==83:
                if x2+5<=w:
                    x2 += 5
                    x1 += 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), 2)
                cv2.imshow("rectangle", temp1)
                l = cv2.waitKey(0)
            elif l==82:
                if y1-5>=0:
                    y1 -= 5
                    y2 -= 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), 2)
                cv2.imshow("rectangle", temp1)
                l = cv2.waitKey(0)
            elif l==84:
                if y2+5<=h:
                    y1 += 5
                    y2 += 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), 2)
                cv2.imshow("rectangle", temp1)
                l = cv2.waitKey(0)
            elif l==81:
                if x1-5>=0:
                    x1 -= 5
                    x2 -= 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), 2)
                cv2.imshow("rectangle", temp1)
                l = cv2.waitKey(0)
            elif l==119:
                if y1-5>=0:
                    y1-=5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)
            elif l == 97:
                if x1 - 5 >= 0:
                    x1 -= 5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)
            elif l == 115:
                if y2 + 5 <= h:
                    y2 += 5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)
            elif l == 100:
                if x2 + 5 <= w:
                    x2 += 5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)
            elif l == 105:
                if y1 + 5 <= y2:
                    y1 += 5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)
            elif l == 106:
                if x1 + 5 <= x2:
                    x1 += 5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)
            elif l == 107:
                if y2 - 5 >= y1:
                    y2 -= 5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)
            elif l == 108:
                if x2 - 5 >= x1:
                    x2 -= 5
                    cv2.rectangle(temp1, (x1, y1), (x2, y2), 2)
                    cv2.imshow("rectangle", temp1)
                    l = cv2.waitKey(0)

            else:
                print(l)
                break
            cv2.destroyAllWindows()
            print(l)


image = cv2.imread("virat.jpeg")
shape(image)