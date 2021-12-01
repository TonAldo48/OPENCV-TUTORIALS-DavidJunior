import numpy as np
import cv2 as cv

img = cv.imread(r'images\j.png',0)
kernel = np.ones((5,5),np.uint8)

## Erosion
dst = cv.erode(img, kernel, iterations= 1)

## Dilate 
dst2 = cv.dilate(dst, kernel, iterations=2)

## Opening // Erosion followed by dilation // usefull for removing noise

dst3 = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

## Closing // Dilation followed by erosion // Useful for removing holes

dst4 = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

## Morphological gradient //Difference between dilation and erosion //

dst5 = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

cv.imshow('dst',dst2)
cv.waitKey(0)

## To get structuring elements , i.e kernel = np.ones((5,5),np.uint8)
## use this 

cv.getStructuringElement(cv.MORPH_CROSS, (5,5))