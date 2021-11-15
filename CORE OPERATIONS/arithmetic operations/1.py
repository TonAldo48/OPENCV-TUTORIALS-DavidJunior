import numpy as np
import cv2 as cv
from time import sleep

img = cv.imread('images\Screenshot (1).png')
img2 = cv.imread('images\Screenshot (2).png')

a = 0.3
b = 1 - a
i = 0.05
n = 0
while True:
    img3 = cv.addWeighted(img2,a,img,b,0)
    cv.imshow('image',img3)
    cv.waitKey(1)
