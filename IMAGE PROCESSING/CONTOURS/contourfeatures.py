import numpy as np
import cv2 as cv

img = cv.imread(r'images\istockphoto-172746852-612x612.jpg',0)

ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv.moments(cnt)
# print( M )


cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# Finding contour area 
area = cv.contourArea(cnt)
# print(area)

# Finding contour perimeter // Second argument is for whether shape is closed or just a curve    
perimeter = cv.arcLength(cnt, True)
print(perimeter)

# Contour approximation
epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt, epsilon, True)

# Finding convex hulls 
hull = cv.convexHull(cnt)

# Checking for convexity of contours
k = cv.isContourConvex(cnt)

# Bounding rectangle  
#  no rotation
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

# Rotated rect 
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),5)

# Min circle
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)

# Fitting eclipse 
# ellipse = cv.fitEllipse(cnt)
# cv.ellipse(img,ellipse,(0,255,0),2)

# Fitting a line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

print(cnt)
dst = cv.drawContours(img, cnt, -1, (0,255,0), 3)
cv.imshow('contour', img)
cv.waitKey(0)