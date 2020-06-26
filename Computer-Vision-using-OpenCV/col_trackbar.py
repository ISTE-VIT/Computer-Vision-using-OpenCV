import cv2
import numpy as np

def callback(x):
    pass
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("image")
cv2.createTrackbar("B","image",0,255,callback)
cv2.createTrackbar("G","image",0,255,callback)
cv2.createTrackbar("R","image",0,255,callback)

while True:
    b=cv2.getTrackbarPos("B","image")
    g=cv2.getTrackbarPos("G","image")
    r=cv2.getTrackbarPos("R","image")
    img[:]=[b,g,r]
    cv2.imshow("image",img)
    k=cv2.waitKey(1)&0xFF
    if k==ord("q"):
        break
cv2.destroyAllWindows()
