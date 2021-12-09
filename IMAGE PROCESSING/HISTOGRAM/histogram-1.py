import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'images\balls.jpg')
img0 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

color = ('b','g','r')

for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])

plt.show()