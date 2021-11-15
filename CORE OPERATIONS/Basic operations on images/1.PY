import numpy as np
import cv2 as cv

img_path = 'images\image3.jpg'
img = cv.imread(img_path)

img[300,500] = [200,300,400] # change the bgr of a pixel, not recommended though
print(img[300,500]) # access one pixel

print(img.item(300,500,2)) # aceesing a pixel
img.itemset((300,500,2), 50)

print(img.item(300,500,2))

print(img.shape[0])
print(img.size)
print(img.dtype)

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

#slitting and saving images #splitting is time costly
b, g, r = cv.split(img)
cv.imwrite('images\blue.jpg',b)
cv.imwrite('images\green.jpg',g)
cv.imwrite('images\red.jpg',r)
print(g.dtype)
img = cv.merge((b,g,r))

cv.imshow('hey',img)
cv.waitKey(0)

