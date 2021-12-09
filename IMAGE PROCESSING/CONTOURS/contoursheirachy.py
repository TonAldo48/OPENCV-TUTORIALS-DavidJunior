import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r'images\star.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 10, 255, cv.THRESH_BINARY)

#Types of modes to use for hierachy
# RETR_LIST, RETR_EXTERNAL, RETR_CCOMP, RETR_TREE
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 6, (255,0,255),3)

print(hierarchy)

plt.subplot(2,2,1),plt.imshow(img,'gray',vmin=0,vmax=255)
plt.subplot(2,2,2),plt.imshow(gray,'gray',vmin=0,vmax=255)
plt.subplot(2,2,3),plt.imshow(thresh,'gray',vmin=0,vmax=255)
plt.title('plot')
plt.xticks([]),plt.yticks([])
plt.show()