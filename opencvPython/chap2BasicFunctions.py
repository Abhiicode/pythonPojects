import cv2
import numpy as np

img = cv2.imread("src/a.jpeg")

imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # for making img black n white

imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)

# Edge detection
imgCanny = cv2.Canny(img,100,100)

# Image dilation(increse the thickness of edges)
kernel = np.ones((5,5),np.uint8)
imgDil = cv2.dilate(imgCanny,kernel,iterations=1)
imgErode = cv2.erode(imgDil,kernel,iterations=1)

#cv2.imshow("Ullu",imgBlur)
#cv2.imshow("Ullu Grey",imgGrey)
cv2.imshow("Ullu Grey Canny",imgCanny)
cv2.imshow("Ullu Grey Canny",img)
cv2.imshow("Ullu Grey Canny dilate",imgDil)
cv2.imshow("Ullu Grey Canny erode",imgErode)

cv2.waitKey(0)

