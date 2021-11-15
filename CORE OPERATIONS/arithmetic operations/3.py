import numpy as np 
import cv2 as cv 

img1 = cv.imread('images\image2.jpg')
img2 = cv.imread('images\opencv-logo-small.png')


# not working well
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10,255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
img1_bg = cv.bitwise_and(roi, roi,mask = mask_inv)
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst

cv.imshow('img', img1)
cv.waitKey(0)
cv.destroyAllWindows()
