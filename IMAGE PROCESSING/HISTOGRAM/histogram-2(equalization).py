import numpy as np 
import cv2 as cv  
import matplotlib.pyplot as plt

img = cv.imread(r'images\balls.jpg',0)

hist, bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_norm = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_norm, color = 'b')
plt.hist(img.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()