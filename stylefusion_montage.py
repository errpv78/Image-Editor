from imutils import build_montages
import random
import cv2
import glob

# construct the argument parse and parse the arguments
images = [cv2.imread(file) for file in glob.glob("/home/err_pv/Desktop/Parikh_linux/Deep Learning/openCV/Image-Editor/default_stlye/*.jpeg")]

for i in range(len(images)):
    cv2.putText(images[i], str(i+1), (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

montages = build_montages(images, (350,250), (5,3))

cv2.imshow("Montage",montages[0])
cv2.waitKey(0)

cv2.imwrite("style_montage.jpeg",montages[0])