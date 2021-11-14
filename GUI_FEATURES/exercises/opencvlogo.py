<<<<<<< HEAD
import cv2 as cv
import numpy as np

img = np.ones((500, 500,3), dtype=np.uint8) # Creating a new black image

t_pts = np.array([[250, 150],[195, 250],[305, 250],[250, 150]], np.int32) # Defining points for dark triangle at the center of the circles
t_pts = t_pts.reshape((-1, 1, 2))

t_pts_2 = np.array([
    [280, 200], [330, 200], [305, 250],
    [280, 200] ], np.int32) # Defining points for the dark triangle cutting a part of the blue circle
t_pts_2 = t_pts_2.reshape((-1, 1, 2))

radius = 35 
thickness = 30

cv.circle(img, (195, 250), radius, (0, 204, 102), thickness) # Green circle
cv.circle(img, (250, 150), radius, (0, 0, 255), thickness) # Red circle
cv.drawContours(img, [t_pts], -1, (0,0,0), -1) # Making a filled contour for first black triangle
cv.circle(img, (305, 250), radius, (255, 128, 0), thickness) # Blue circle
cv.drawContours(img, [t_pts_2], -1, (0,0,0), -1) # Making a filled contour for second black triangle

font = cv.FONT_HERSHEY_PLAIN
cv.putText(img, "OpenCV",(125, 360), font, 4, (255,255,255), 5 ) # Putting 'OpenCV' string on the image

cv.imshow('Window', img)

if cv.waitKey(0) == ord('q'):
    exit()

=======
import cv2 as cv
import numpy as np

img = np.ones((500, 500,3), dtype=np.uint8) # Creating a new black image

t_pts = np.array([[250, 150],[195, 250],[305, 250],[250, 150]], np.int32) # Defining points for dark triangle at the center of the circles
t_pts = t_pts.reshape((-1, 1, 2))

t_pts_2 = np.array([
    [280, 200], [330, 200], [305, 250],
    [280, 200] ], np.int32) # Defining points for the dark triangle cutting a part of the blue circle
t_pts_2 = t_pts_2.reshape((-1, 1, 2))

radius = 35 
thickness = 30

cv.circle(img, (195, 250), radius, (0, 204, 102), thickness) # Green circle
cv.circle(img, (250, 150), radius, (0, 0, 255), thickness) # Red circle
cv.drawContours(img, [t_pts], -1, (0,0,0), -1) # Making a filled contour for first black triangle
cv.circle(img, (305, 250), radius, (255, 128, 0), thickness) # Blue circle
cv.drawContours(img, [t_pts_2], -1, (0,0,0), -1) # Making a filled contour for second black triangle

font = cv.FONT_HERSHEY_PLAIN
cv.putText(img, "OpenCV",(125, 360), font, 4, (255,255,255), 5 ) # Putting 'OpenCV' string on the image

cv.imshow('Window', img)

if cv.waitKey(0) == ord('q'):
    exit()

>>>>>>> 1689d00278c78bd22cc2e05912fecfb338f63262
cv.destroyAllWindows()