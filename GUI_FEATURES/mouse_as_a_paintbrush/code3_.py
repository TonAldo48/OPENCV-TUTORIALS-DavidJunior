import cv2 as cv
import numpy as np

ix, iy = -1, -1
drawing = False
mode = True

def drawcircle(event, x, y, flags, params):
    global ix, iy, mode, drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event ==  cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == 0:
                cv.circle(img, (x,y), 5, (220, 40,50), 3)
            else:
                cv.rectangle(img,(x,y), (ix,iy), (220, 40,50), 3)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == 0:
                cv.circle(img, (x,y), 5, (220, 40,50), 3)
        else:
            cv.rectangle(img,(x,y), (ix,iy), (220, 40,50), 3)

img = np.zeros((512,512,3), dtype=np.uint8)
cv.namedWindow('Window')
cv.setMouseCallback('Window',drawcircle)    

while True:
    cv.imshow('Window',img)
    k = cv.waitKey(1) 

    if k == ord('c'):
        mode = not mode

    if k == ord('f'):
        break


cv.destroyAllWindows()