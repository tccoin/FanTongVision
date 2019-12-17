import cv2
import pymynt
import numpy as np

pymynt.init_camera('raw')
while True:
    mat = pymynt.get_depth_image()
    # gray  = cv2.cvtColor(mat, cv2.COLOR_RGB2GRAY)
    # binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)[1]
    # print(binary.shape)
    # contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # if not contours is None:
    #     good_contours = []
    #     for contour in contours:
    #         area=cv2.contourArea(contour)
    #         x,y,w,h=cv2.boundingRect(contour)
    #         rect_area=w*h
    #         extent=float(area)/rect_area
    #         if extent>0.65 and rect_area>40000:
    #             good_contours += [contour]
    #             cv2.putText(mat, str(rect_area), (x, y+10),
    #                         cv2.FONT_HERSHEY_PLAIN, 1.2, (200, 200, 200), 1
    #                         )
    #             cv2.rectangle(mat, (x, y), (x+w, y+h), (0, 0, 200), 2)
    #     cv2.drawContours(mat, good_contours, -1, (255,255,0), thickness=2)
        # cv2.imshow('test',mat)
    cv2.imshow('test',mat)
    cv2.waitKey(18)