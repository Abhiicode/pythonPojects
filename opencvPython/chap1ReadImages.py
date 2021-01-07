import cv2

# img = cv2.imread("src/a.jpeg")

# cv2.imshow("Ullu",img)
# cv2.waitKey(0)


cap = cv2.VideoCapture("src/video.mp4")
# for video cam 
# cap = cv2.VideoCapture(0)
# for setting width , height and brightness
# cap.set(3,640) / width
# cap.set(4,480) / height
# cap.set(10,100) /brighness

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


