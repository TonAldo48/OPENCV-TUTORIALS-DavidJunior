import cv2 as cv
import numpy as np

def nothing(x):
    pass
cv.namedWindow('Paint Application')
cv.createTrackbar('Red', 'Paint Application', 0,255, nothing)
cv.createTrackbar('Green', 'Paint Application', 0,255, nothing)
cv.createTrackbar('Blue', 'Paint Application', 0,255, nothing)
cv.createTrackbar('Radius', 'Paint Application', 0,10, nothing)

ix, iy = -1, -1
drawing = False

def pointer(event, x, y, flags, param):
    global ix, iy, drawing, color_, thickness_

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy =  x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img, (x, y), thickness_, tuple(color_), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img, (x, y), thickness_, tuple(color_), -1)

img = np.zeros((512,512,3), dtype=np.uint8)
cv.setMouseCallback('Paint Application', pointer)

while True:
    
    cv.imshow('Paint Application', img)

    r = cv.getTrackbarPos('Red', 'Paint Application')
    g = cv.getTrackbarPos('Green', 'Paint Application')
    b = cv.getTrackbarPos('Blue', 'Paint Application')

    thickness_ = cv.getTrackbarPos('Radius', 'Paint Application')

    color_ = [b, g, r]

    k = cv.waitKey(1) & 0xFF
    
    if k == ord('p'):
        break

    print(tuple(color_))

cv.destroyAllWindows()