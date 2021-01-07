import cv2
import numpy as np

img = cv2.imread("src/card.jpg")
print(img.shape)

imgResize = cv2.resize(img,(640,425))


pts1 = np.float32([
    [60,177],
    [255,73],
    [235,425],
    [437,313]
])

width,height = 270,400
pts2= np.float32([
    [0,0],
    [width,0],
    [0,height],
    [width,height]
])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
#cv2.imwrite("new.jpg",imgResize)

imgOut = cv2.warpPerspective(imgResize,matrix,(width,height))
cv2.imwrite("src/joker.jpg",imgOut)
cv2.imshow("Image",imgOut)
cv2.imshow("Image new",imgResize)
cv2.waitKey(0)