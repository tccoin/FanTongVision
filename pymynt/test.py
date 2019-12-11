import cv2
import pymynt
import numpy as np

pymynt.init_camera()
while True:
    mat = pymynt.get_depth_image()
    cv2.imshow('test',mat)
    cv2.waitKey(17)