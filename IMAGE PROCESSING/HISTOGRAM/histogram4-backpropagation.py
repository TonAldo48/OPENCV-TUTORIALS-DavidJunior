import numpy as np 
import cv2 as cv

roi = cv.imread(r'images\balls - roi.jpg')
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

target = cv.imread(r'images\balls.jpg')
hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)

roi_hist = cv.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
dst = cv.calcBackProject([hsvt],[0,1],roi_hist,[0,180,0,256],1)

disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(dst,-1,disc,dst)

ret, thresh = cv.threshold(dst,50,255,0)
thresh = cv.merge((thresh,thresh,thresh))
res = cv.bitwise_and(target, thresh)

res = np.vstack((target, thresh, res))
cv.imwrite('res.jpg',res)
cv.imshow('win',res)
cv.waitKey(0)