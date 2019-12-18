import cv2
import numpy as np

def printDepth(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(ori[y,x],img[y,x])
        cv2.circle(img, (x, y), 100, 100, -1)

ori = cv2.imread('data/depth_gray.jpg')
img = ori/np.max(ori)
cv2.imshow('depth', img)
cv2.setMouseCallback('depth', printDepth)
cv2.waitKey(-1)