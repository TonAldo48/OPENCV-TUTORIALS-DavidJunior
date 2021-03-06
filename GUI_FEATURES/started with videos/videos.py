import cv2 as cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera cannot be opened')
    exit()

while True:
       
    ret, frame = cap.read()

    if ret == False:
        print('Could not read frame')
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video window',gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()