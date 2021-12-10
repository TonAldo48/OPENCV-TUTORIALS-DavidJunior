import numpy as np 
import cv2 as cv  
import matplotlib.pyplot as plt
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('images\overandunderexposed mimages'):
    f.extend(filenames)
    break

print(f)

imgs = []

for i in range(len(f)):
    img = cv.imread(r'images\overandunderexposed mimages\{}'.format(f[i]))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hist, bins = np.histogram(img.flatten(),256,[0,256])

    cdf = hist.cumsum()
    cdf_norm = cdf * float(hist.max()) / cdf.max()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    imgs.append(cdf[img])
    print(type(imgs[i]))

    plt.subplot(2,2,i+1),plt.imshow(img)
    plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.show()