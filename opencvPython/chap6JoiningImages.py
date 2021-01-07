import cv2
import numpy as np

img = cv2.imread("src/joker.jpg")


# horizontal merge
imgHor = np.hstack((img,img))
cv2.imshow("Horizontal Merge",imgHor)

#vertical merge
imgVer = np.vstack((img,img))
cv2.imshow("Vertical Merge",imgVer)


cv2.waitKey(0)