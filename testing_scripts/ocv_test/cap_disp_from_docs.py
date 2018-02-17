import numpy as np
import cv2

# Testing script. Successfully runs on python 2 and capture device
# Custom compiled OpenCV did not open video device successfully.
# From official documentation https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# Works even though I'm using an earlier OpenCV version.

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Operate on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display resulting frame
    cv2.imshow('frame', gray)
    # cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
#        cv2.imwrite('img_color.png',frame)
#        cv2.imwrite('img_gray.png', gray)
        break

# When done, release capture
cap.release()
cv2.destroyAllWindows()
