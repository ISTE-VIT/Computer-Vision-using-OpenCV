import cv2
import numpy as np



def callback(x):
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,callback)
cv2.createTrackbar("UH","Tracking",255,255,callback)
cv2.createTrackbar("LS","Tracking",0,255,callback)
cv2.createTrackbar("US","Tracking",255,255,callback)
cv2.createTrackbar("LV","Tracking",0,255,callback)
cv2.createTrackbar("UV","Tracking",255,255,callback)

while True:
    img=cv2.imread("smarties.png")
    l_h=cv2.getTrackbarPos("LH","Tracking")
    u_h=cv2.getTrackbarPos("UH","Tracking")
    l_s=cv2.getTrackbarPos("LS","Tracking")
    u_s=cv2.getTrackbarPos("US","Tracking")
    l_v=cv2.getTrackbarPos("LV","Tracking")
    u_v=cv2.getTrackbarPos("UV","Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(img,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("image",img)
    cv2.imshow("res",res)
    cv2.imshow("mask",mask)

    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()

