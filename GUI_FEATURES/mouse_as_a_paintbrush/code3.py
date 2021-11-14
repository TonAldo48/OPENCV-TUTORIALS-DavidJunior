import cv2 as cv
import numpy as np

drawing = False
mode = True

ix, iy = -1, -1

def draw_circle(event, x, y, flags, param):
    global ix,iy,mode,drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode == True:
                cv.rectangle(img, (ix,iy), (x, y),(255, 9, 9), -1)
            else:
                cv.circle(img, (x,y),5,(0,255,0), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix,iy), (x,y),(255, 9, 9), -1)
        else:
            cv.circle(img, (x,y),5,(0,255,0),-1)

img = np.zeros((512,512,3), dtype=np.uint8)
cv.namedWindow('Window')
cv.setMouseCallback('Window',draw_circle)

while True:
    cv.imshow('Window', img)
    k = cv.waitKey(1) & 0xFF
    
    if k == ord('m'):
        mode = not mode
    if k == 27:
        break

cv.destroyAllWindows()