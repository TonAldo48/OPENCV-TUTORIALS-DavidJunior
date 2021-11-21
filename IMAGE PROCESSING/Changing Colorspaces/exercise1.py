import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lb = np.array([110, 50, 50])
    hb = np.array([130, 255, 255])

    lg = np.array([36, 25, 25])
    ug = np.array([86, 255, 255])

    lr = np.array([0, 100, 20])
    ur = np.array([10, 255, 255])

    mask1 = cv.inRange(hsv, lb, hb)
    mask2 = cv.inRange(hsv, lg, ug)
    mask3 = cv.inRange(hsv, lr, ur)
    
    masks_add = mask1 + mask2 + mask3

    res = cv.bitwise_and(frame, frame, mask = masks_add)

    cv.imshow('frame', frame)
    cv.imshow('mask1',masks_add)
    cv.imshow('window', res)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cv.destroyAllWindows()