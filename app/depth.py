import cv2
import pymynt
import numpy as np
import time

watching_point = None


def printDepth(event, x, y, flags, param):
    global watching_point
    if event == cv2.EVENT_FLAG_LBUTTON:
        print((x, y), ' :', mat[y, x])
        watching_point = (x, y)


pymynt.init_camera('raw')
while True:
    mat = pymynt.get_depth_image()
    if mat.shape[0] < 10:
        continue
    print(mat.shape)
    out = mat/np.max(mat)*255
    out = out.astype('uint8')
    out = cv2.cvtColor(out, cv2.COLOR_GRAY2RGB)
    if not watching_point is None:
        _ = watching_point
        print(_, ' depth :', mat[_[1], _[0]])
        cv2.circle(out, _, 8, (100, 100, 200), 2)
    cv2.imshow('depth', out)
    cv2.setMouseCallback('depth', printDepth)
    cv2.waitKey(18)
