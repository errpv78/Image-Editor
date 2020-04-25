import cv2
import imutils
import glob
import numpy as np

def color_transfer(source, target, clip=True, preserve_paper=True):
	source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
	target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")

	(l, a, b) = cv2.split(source)
	(lMeanSrc, lStdSrc) = (l.mean(), l.std())
	(aMeanSrc, aStdSrc) = (a.mean(), a.std())
	(bMeanSrc, bStdSrc) = (b.mean(), b.std())

	(l, a, b) = cv2.split(target)
	(lMeanTar, lStdTar) = (l.mean(), l.std())
	(aMeanTar, aStdTar) = (a.mean(), a.std())
	(bMeanTar, bStdTar) = (b.mean(), b.std())

	(l, a, b) = cv2.split(target)
	l -= lMeanTar
	a -= aMeanTar
	b -= bMeanTar

	l = (lStdSrc / lStdTar) * l
	a = (aStdSrc / aStdTar) * a
	b = (bStdSrc / bStdTar) * b

	l += lMeanSrc
	a += aMeanSrc
	b += bMeanSrc

	l = np.clip(l, 0,255)
	a = np.clip(a, 0,255)
	b = np.clip(b, 0,255)

	transfer = cv2.merge([l, a, b])
	transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)

	return transfer


def fuse_image(target):
	c = input("Enter style image from default (press 1), custom image (press 2): ")
	if c=="1":
		montage = cv2.imread("style_montage.jpeg")
		cv2.imshow("Select image number to fuse style from", montage)
		choice = cv2.waitKey(0)
		cv2.destroyAllWindows()
		choice = int(choice)-49

		images = [cv2.imread(file) for file in glob.glob("/home/err_pv/Desktop/Parikh_linux/Deep Learning/openCV/Image-Editor/default_stlye/*.jpeg")]
		source = images[choice]
		cv2.imshow("Source Press any key to continue", source)
		extra = cv2.waitKey(0)
		cv2.destroyAllWindows()

	else:
		source = None
		while source is None:
			image_name = input("Enter image name(with extension): ")
			source = cv2.imread(image_name)
			if source is None:
				print("Image not found")
			else:
				(h, w, d) = source.shape
				r = 300 / h
				dim = (int(r * w), 300)
				source = cv2.resize(source, dim)
				cv2.imshow("Press any key to continue", source)
				l = cv2.waitKey(0)
				if l:
					cv2.destroyAllWindows()
				else:
					cv2.destroyAllWindows()

	transfer = color_transfer(source, target)
	cv2.imshow("Edited image Press any key to continue", transfer)
	l = cv2.waitKey(0)
	cv2.destroyAllWindows()
	return transfer
