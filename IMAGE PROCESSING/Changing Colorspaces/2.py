import cv2 as cv
import numpy as np

###------------------------------SCALING----------------------------####

img = cv.imread('images\Screenshot (2).png')
res = cv.resize(img,None, fx = 0.4, fy = 0.4, interpolation = cv.INTER_LINEAR)

###------------------------------TRANSLATINO----------------------------####

cols, rows = img.shape
x, y = 100, 50
M = np.float32([[1, 0, x],[0,1,y]])
dst = cv.warpAffine(img, M, (cols, rows)) # (width, height) width = no of cols, height = no of rows

###------------------------------ROTATION----------------------------####

x_centre = (cols-1)/2.0
y_centre = (rows-1)/2.0

M1 = cv.getRotationMatrix2D((x_centre, y_centre), 90,1)

###------------------------------AFFINE TRANSFORMATION----------------------------####

rows, cols, ch = img.shape

pts1 = np.float([[50,50],[200,50],[50,200]]) # Three perpendicular parallel lines from image
pts2 = np.float32([[10,100],[200,50],[100,250]]) # Resulting 3 points

M2 = cv.getAffineTransform(pts1,pts2) # returns a 2 x 3 matrix 

dst1 = cv.warpAffine(img, M2, (cols, rows))

###------------------------------PERSPECTIVE TRANSFORM----------------------------####

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) # four points from image where 3 are not collinear
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M3 = cv.getAffineTransform(pts1, pts2)

dst3 = cv.warpPerspective(img, M3, (300,300)) # new img size