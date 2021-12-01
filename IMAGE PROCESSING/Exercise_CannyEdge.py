import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('Canny Edge Detection')
cv.createTrackbar('Toggle', 'Canny Edge Detection',0,1, nothing)
cv.createTrackbar('Min Thres', 'Canny Edge Detection',0,200, nothing)
cv.createTrackbar('Max Thres', 'Canny Edge Detection',0,200, nothing)

img_path = r'images\image3.jpg'
img = cv.imread(img_path)

while True:
    toggle_ = cv.getTrackbarPos('Toggle', 'Canny Edge Detection')
    min_ = cv.getTrackbarPos('Min Thres', 'Canny Edge Detection')
    max_ = cv.getTrackbarPos('Max Thres', 'Canny Edge Detection')

    edges = cv.Canny(img, min_, max_)
    
    if toggle_ == 1:
        cv.imshow('Canny Edge Detection', edges)  
    else:
        cv.imshow('Canny Edge Detection', img)

    k = cv.waitKey(1)

    if k == ord('p'):
        break

cv.destroyAllWindows()