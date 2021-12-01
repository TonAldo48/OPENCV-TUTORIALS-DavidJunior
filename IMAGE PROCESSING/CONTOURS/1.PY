import numpy as np 
import cv2 as cv

img = cv.imread('images\image3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thres = cv.threshold(gray, 127,255,0)
contours, hierarchy = cv.findContours(thres, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# cnt = contours[4]
# dst = cv.drawContours(gray, [cnt], 0, (0,255,0),1)

dst = cv.drawContours(img, contours, -1, (0,255,0), 3)

cv.imshow('dst',dst)
cv.waitKey(0)