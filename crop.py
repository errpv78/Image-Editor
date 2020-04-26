import cv2
import numpy as np


def four_point_transform(image, pts):
    #  image  variable is image we want to apply perspective
    #  transform to. And the pts  list is the list of four
    #  points that contain the ROI of the image we want to
    #  transform.

    # obtain a consistent order of points and unpack them
    # individually
    pts = np.array(pts, dtype="float32")
    tl, tr, br, bl = pts[0], pts[1], pts[2], pts[3]

    # compute the width of the new image, which will be
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be
    # maximum distance between top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have dimensions of new image, construct
    # set of destination points to obtain "birds eye view",
    # (i.e. top-down view) of the image, again specifying
    # points in top-left, top-right, bottom-right, and
    # bottom-left order.

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # compute perspective transform matrix and then apply
    # it

    M = cv2.getPerspectiveTransform(pts, dst)

    # This function requires two arguments, rect , which is
    # list of 4 ROI points in original image, and dst ,
    # which is our list of transformed points. The
    # cv2.getPerspectiveTransform  function returns M ,
    # which is actual transformation matrix.
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    cv2.imshow("Cropped", warped)
    l = cv2.waitKey()
    if l==0:
        cv2.destroyAllWindows()
    else:
        cv2.destroyAllWindows()
    # return the warped image
    return warped

def crop_img(image):

    (h,w,d) = image.shape
    cx, cy = w//2,h//2
    temp = image
    corners = [[cx-30,cy-30], [cx+30, cy-30], [cx+30, cy+30], [cx-30, cy+30]]
    point = 0
    l = -1
    while l!=13:
        temp = image.copy()
        if l==-1:
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)

        elif l==83:
            if corners[point][0]+5<=w:
                corners[point][0]+=5
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)

        elif l==82:
            if corners[point][1]-5>=0:
                corners[point][1]-=5
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)
        elif l==84:
            if corners[point][1]+5<=h:
                corners[point][1]+=5
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)
        elif l==81:
            if corners[point][0]-5>=0:
                corners[point][0]-=5
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)
        elif l==49:
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 3, (255, 255, 255), -1)
            point = 0
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)
        elif l==50:
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 3, (255, 255, 255), -1)
            point = 1
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)
        elif l==51:
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 3, (255, 255, 255), -1)
            point = 2
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)
        elif l==52:
            cv2.line(temp, (corners[0][0], corners[0][1]), (corners[1][0], corners[1][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[1][0], corners[1][1]), (corners[2][0], corners[2][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[2][0], corners[2][1]), (corners[3][0], corners[3][1]), (0, 0, 0), 2)
            cv2.line(temp, (corners[3][0], corners[3][1]), (corners[0][0], corners[0][1]), (0, 0, 0), 2)
            cv2.circle(temp, (corners[point][0], corners[point][1]), 3, (255, 255, 255), -1)
            point = 3
            cv2.circle(temp, (corners[point][0], corners[point][1]), 5, (255, 255, 255), -1)
            cv2.imshow("Select corners 1-tl,2-tr,3-br,4-bl; Press enter when done", temp)
            l = cv2.waitKey(0)
        else:
            break
    return four_point_transform(image, corners)










# image = cv2.imread("trip.jpg")
# crop_img(image)
