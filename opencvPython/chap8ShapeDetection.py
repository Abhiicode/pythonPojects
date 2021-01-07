import cv2
import numpy as np


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgCon,cnt,-1,(255,0,0),3)

path = 'src/shapes.jpg'
img = cv2.imread(path)
imgCon = img.copy()
# img = cv2.resize(img,(512,512))

imgGray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

imgBlank = np.zeros_like(imgCanny)

cv2.imshow("ImgBlur",imgCanny)
cv2.imshow("ImgBlank",imgBlank)

cv2.waitKey(0)