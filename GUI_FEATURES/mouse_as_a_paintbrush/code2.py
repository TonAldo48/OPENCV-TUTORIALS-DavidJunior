<<<<<<< HEAD
import cv2 as cv
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x,y), 100,(255, 0, 0), -1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('Window')
cv.setMouseCallback('Window', draw_circle)

while True:
    cv.imshow('Window', img)
    if cv.waitKey(1) == ord('q'):
        break

=======
import cv2 as cv
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x,y), 100,(255, 0, 0), -1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('Window')
cv.setMouseCallback('Window', draw_circle)

while True:
    cv.imshow('Window', img)
    if cv.waitKey(1) == ord('q'):
        break

>>>>>>> 1689d00278c78bd22cc2e05912fecfb338f63262
cv.destroyAllWindows()