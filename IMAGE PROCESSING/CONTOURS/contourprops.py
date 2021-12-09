import numpy as np
import cv2 as cv

img = cv.imread(r'images\istockphoto-172746852-612x612.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.imread(r'images\istockphoto-172746852-612x612.jpg',0)

ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)

cnt = contours
print(cnt)
x,y,w,h = cv.boundingRect(cnt[0])
aspect_ratio = float(w)/h
print(aspect_ratio)

area = cv.contourArea(cnt[0])
rect_area = w*h
extent = area/rect_area

hull = cv.convexHull(cnt[0])
hull_area = cv.contourArea(hull)
solidity = area/hull_area

# Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
equi_diameter = np.sqrt(4*area/np.pi)

(x,y), (MA,ma), angle = cv.fitEllipse(cnt[1])

mask = np.zeros(imgray.shape,np.uint8)
cv.drawContours(mask,[cnt[0]],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask)) # Returns **row,column**
#pixelpoints = cv.findNonZero(mask) # Returns **colomn, row**

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray,mask = mask)
