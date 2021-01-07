import cv2
import numpy as np

# Color detection

def empty(a):
    pass


img = cv2.imread("src/bg.png")

img = cv2.resize(img,(540,245))

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,270)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV img",imgHsv)
cv2.imshow("Img",img)
while True:
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    upper = np.array([h_max,s_max,v_max])
    lower = np.array([h_min,s_min,v_min])
    mask = cv2.inRange(imgHsv,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)

