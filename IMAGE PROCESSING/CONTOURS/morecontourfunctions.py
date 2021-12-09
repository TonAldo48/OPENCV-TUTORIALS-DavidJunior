import numpy as np
import cv2 as cv

img = cv.imread('images\star.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 125, 255, 0)
contours, hierarchy = cv.findContours(thresh, 2, 1)
cnt = contours[0]
print(cnt)
hull = cv.convexHull(cnt)
print(hull)
defects = cv.convexityDefects(cnt, hull)
print(type(defects))
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]

    