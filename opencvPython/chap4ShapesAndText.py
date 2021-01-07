import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(100,100),(img.shape[1],img.shape[0]),(0,234,89),3)
cv2.rectangle(img,(0,0),(100,100),(0,0,255),cv2.FILLED)

cv2.circle(img,(150,150),70,(255,0,0),3)

cv2.putText(img, "OPENCV" ,(150,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,123,150),1)
cv2.imshow("Image",img)
cv2.waitKey(0)