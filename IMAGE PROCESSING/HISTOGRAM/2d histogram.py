import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r'images\folder\3.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0,1], None, [180,256],[0,180,0,256])

plt.imshow(hist, interpolation='nearest')
plt.show()