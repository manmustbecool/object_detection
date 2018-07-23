# pip install opencv-python

import cv2

print(cv2.__file__)

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
