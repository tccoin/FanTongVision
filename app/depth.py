import cv2
import pymynt
import numpy as np

pymynt.init_camera('raw')
while True:
    mat = pymynt.get_depth_image()
    matfix = mat/np.max(mat) #convert val to [0, 255]
    cv2.imshow('depth',matfix)
    cv2.waitKey(18)