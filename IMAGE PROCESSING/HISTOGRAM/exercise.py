import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'images\balls.jpg')

color = ('b','g','r')

for i, col in enumerate(color):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])

plt.show()