import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv.inRange(hsv, lower_blue, upper_blue)

    res = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow('Frame',frame)
    cv.imshow('Mask',mask)
    cv.imshow('Res',res)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cv.destroyAllWindows()
