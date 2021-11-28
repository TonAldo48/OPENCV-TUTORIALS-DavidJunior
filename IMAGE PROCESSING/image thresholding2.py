import numpy as np 
import cv2 as cv  
# from matplotlib import pyplot as plt

img = cv.imread('images\image3.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

th1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
print(th1)
cv.imshow('frame',th1)
cv.waitKey(0)