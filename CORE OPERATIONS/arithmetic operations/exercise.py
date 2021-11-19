import glob
import cv2 as cv
import numpy as np
from time import sleep

img_folder = glob.glob(r"images\folder\*")
n = len(img_folder)
a = 1
b = 0

while True:
    for i in range(n):
        if i < n-1:
            img1 = cv.imread(img_folder[i])
            img2 = cv.imread(img_folder[i+1])
            while True:
                img3 = cv.addWeighted(img1,a,img2,b,0)
                cv.imshow('slideshow',img3)
                cv.waitKey(1)
                if a >= 0 and a <= 1 and b >= 0 and b <= 1:
                    a -= 0.01
                    b = 1 - a
                else:
                    a = 1
                    b = 0
                    break       
        else:
            sleep(2)