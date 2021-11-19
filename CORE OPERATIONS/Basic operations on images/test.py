import numpy as np
import cv2 as cv

def capture():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break
        cv.imshow('window', frame)

        k = cv.waitKey(1)
        if k == ord('c'):
            cv.imwrite('CORE OPERATIONS\Basic operations on images\image.jpg', frame)

        elif k == ord('p'):
            break

    cap.release()
    cv.destroyAllWindows

capture()
