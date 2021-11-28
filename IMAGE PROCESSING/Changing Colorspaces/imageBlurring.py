import numpy as np
import cv2 as cv

img = cv.imread(r'images\image3.jpg')

## 1. AVERAGING 
## Convulving an image with a normalized box filter 
blur = cv.blur(img,(5,5))

## 2. Gaussian BLurring
## Uses the Gaussian kernel / Gaussian weighted average
## Create a Gaussian kernal using blur = cv.GaussianBlur(img,(5,5),0)

blur2 = cv.GaussianBlur(img,(5,5),0)

## Median Blurring 
## Replaces central value with the median of all the pixels in the kernel area  
## Reduces noise effectively

median = cv.medianBlur(img, 5)

## Bilateral Filtering 
## Makes use of two Gaussian Filters in space. 1. the normal one and 2. One a function of
##  pixel difference
## note: d = 5 for real time applications and d = 9 for offline apps

b_blur = cv.bilateralFilter(img, 9, 75, 75)

cv.imshow('ble',b_blur)


cv.waitKey(0)
