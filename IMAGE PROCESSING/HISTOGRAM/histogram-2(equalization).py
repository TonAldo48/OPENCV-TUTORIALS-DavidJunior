import numpy as np 
import cv2 as cv  
import matplotlib.pyplot as plt

img = cv.imread(r'images\overandunderexposed mimages\overx2.jpg',0)

hist, bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_norm = cdf * float(hist.max()) / cdf.max()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]
print(type(img2))
cv.imshow('t',img2)

plt.plot(cdf_norm, color = 'b')
plt.hist(img2.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()