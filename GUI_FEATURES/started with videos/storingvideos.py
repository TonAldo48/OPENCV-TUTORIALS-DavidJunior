<<<<<<< HEAD
import cv2 as cv

cap =  cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 30, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == False:
        print("could not recieve frame")
        break

    cv.imshow('totle',frame)
    out.write(frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
=======
import cv2 as cv

cap =  cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 30, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == False:
        print("could not recieve frame")
        break

    cv.imshow('totle',frame)
    out.write(frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
>>>>>>> 1689d00278c78bd22cc2e05912fecfb338f63262
cv.destroyAllWindows()