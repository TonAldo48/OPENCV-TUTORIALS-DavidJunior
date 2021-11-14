import numpy as np
import cv2 as cv
import sys

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX

while cap.isOpened():

    # img = np.zeros((500, 500, 3), np.uint8)

    ret, img =  cap.read()

    cv.line(img,(0,0),(500, 500), (255,125,0),5)
    cv.rectangle(img,(250,250),(350,350), (255, 250, 100), -1)
    cv.circle(img, (250,250), 50, (240, 10, 250), -1)
    pts = np.array([[20,20], [20,30], [40, 30], [50, 60]], dtype=np.int32)
    pts = pts.reshape(-1, 1, 2)
    cv.polylines(img, [pts], True, (255, 60, 44))

    cv.putText(img, "ERULONA", (10, 250), font, 4, (240, 50, 140), 4, cv.LINE_AA)

    cv.imshow("frame name", img)

    if cv.waitKey(1) == ord('q'):
        sys.exit()
