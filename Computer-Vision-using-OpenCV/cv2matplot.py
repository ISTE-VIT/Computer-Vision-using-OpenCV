import cv2
from matplotlib import pyplot as plt


img= cv2.imread("home.jpg",-1)
img1=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow("image",img)
plt.imshow(img)
plt.imshow(img1)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
