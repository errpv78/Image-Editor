import cv2
import numpy as np

def shape(image):
    (h,w,d) = image.shape
    temp = image
    choice = input("Enter Shape (1 Rectangle, 2 Circle, 3 Text, 4 Exit): ")
    choice = int(choice)
    x1,y1 = w//2-20,h//2-20
    x2,y2 = w//2+20,h//2+20
    t = 1
    if choice==1:
        l = -1
        while l!=49:
            temp1 = temp.copy()
            if l==-1:
                cv2.rectangle(temp1,(x1,y1),(x2,y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l==83:
                if x2+5<=w:
                    x2 += 5
                    x1 += 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l==82:
                if y1-5>=0:
                    y1 -= 5
                    y2 -= 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l==84:
                if y2+5<=h:
                    y1 += 5
                    y2 += 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l==81:
                if x1-5>=0:
                    x1 -= 5
                    x2 -= 5
                cv2.rectangle(temp1, (x1,y1), (x2,y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l==119:
                if y1-5>=0:
                    y1-=5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l == 97:
                if x1 - 5 >= 0:
                    x1 -= 5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l == 115:
                if y2 + 5 <= h:
                    y2 += 5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l == 100:
                if x2 + 5 <= w:
                    x2 += 5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l == 105:
                if y1 + 5 <= y2:
                    y1 += 5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l == 106:
                if x1 + 5 <= x2:
                    x1 += 5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l == 107:
                if y2 - 5 >= y1:
                    y2 -= 5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l == 108:
                if x2 - 5 >= x1:
                    x2 -= 5
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)", temp1)
                l = cv2.waitKey(0)
            elif l==116:
                t += 1
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==32:
                if t>12:
                    t -= 1
                cv2.rectangle(temp1, (x1, y1), (x2, y2), (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,a,s,d) to inc size, (i,j,k,l) to dec size, 1 to finish, (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)

            else:
                cv2.destroyAllWindows()
                break
        temp = temp1

    elif choice==2:
        l = -1
        cx = w//2
        cy = h//2
        r = 50
        t = 1
        while l!=49:
            temp1 = temp.copy()
            if l==-1:
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==83:
                if cx+5+r<=w:
                    cx += 5
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==82:
                if cy-5-r>=0:
                    cy -= 5
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==84:
                if cy+5+r<=h:
                    cy += 5
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==81:
                if cx-5-r>=0:
                    cx -= 5
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==119:
                if cx-5-r>=0 and cx+r+5<=w and cy+5+r<=h and cy-5-r>=0:
                    r += 5
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==119:
                if r>=5:
                    r -= 5
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==116:
                t += 1
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                # cv2.destroyAllWindows()
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            elif l==32:
                if t>1:
                    t -= 1
                cv2.circle(temp1, (cx, cy), r, (0, 0, 0),thickness=t)
                cv2.imshow("Arrow keys to move, (w,s to inc dec size) (t,space to inc dec thickness)",temp1)
                l = cv2.waitKey(0)
            else:
                cv2.destroyAllWindows()
                break
        temp = temp1
    elif choice==3:
        l = -1
        x = w//2
        y = h//2
        f = 2
        t = 2
        string = input("Enter text: ")
        while l!=49:
            temp1 = temp.copy()
            if l==-1:
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==83:
                if x+5<=w:
                    x += 5
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==82:
                if y-5>=0:
                    y -= 5
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==84:
                if y+5<=h:
                    y += 5
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==81:
                if x-5>=0:
                    x -= 5
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==116:
                f+=1
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==32:
                if f>1:
                    f-=1
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==119:
                t += 1
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)
            elif l==115:
                if t>1:
                    t -= 1
                cv2.putText(temp1, string, (x, y),cv2.FONT_HERSHEY_SIMPLEX, fontScale=f, color=(0, 0, 0), thickness=t)
                cv2.imshow("Arrow keys to move, (t, inc size, space to dec size)", temp1)
                l = cv2.waitKey(0)

            else:
                cv2.destroyAllWindows()
                break
        temp = temp1
        # cv2.imshow("t",temp)
        # cv2.waitKey(0)
    cv2.destroyAllWindows()
    return temp

# image = cv2.imread("trip.jpg")
# shape(image)