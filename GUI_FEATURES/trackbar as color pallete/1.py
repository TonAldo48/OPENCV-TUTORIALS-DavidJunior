import cv2 as cv
import numpy as np

def nothing(x):
    pass

img = np.zeros((512, 512, 3), dtype=np.uint8)
cv.namedWindow('Window')

cv.createTrackbar('Red', 'Window', 0, 255, nothing)
cv.createTrackbar('Green', 'Window', 0, 255, nothing)
cv.createTrackbar('Blue', 'Window', 0, 255, nothing)

switch = '0:OFF\n1:ON'
cv.createTrackbar(switch, 'Window', 0, 1, nothing)

while True:
    cv.imshow('Window', img)
    k = cv.waitKey(1)
    if k == ord('p'):
        break

    r = cv.getTrackbarPos('Red', 'Window')
    g = cv.getTrackbarPos('Green', 'Window')
    b = cv.getTrackbarPos('Blue', 'Window')
    s = cv.getTrackbarPos(switch,'Window')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]