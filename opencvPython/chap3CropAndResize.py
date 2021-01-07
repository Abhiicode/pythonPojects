import cv2
import numpy as np

img = cv2.imread("src/lambo.jpg")
print(img.shape)

imgResize = cv2.resize(img,(1100,550))
print(imgResize.shape)

imgCroped = imgResize[0:225,200:1100]

#cv2.imshow("Car",img)
cv2.imshow("Car resized",imgResize)
cv2.imshow("Car Cropped",imgCroped)

cv2.waitKey(0)
