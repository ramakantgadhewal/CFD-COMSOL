import cv2
cap = cv2.VideoCapture(0)
from time import sleep




grabbed,frame = cap.read()
cv2.imshow("frame",frame)
# while grabbed:
    # grabbed,frame = cap.read()
    # cv2.imshow("frame",frame)

    # sleep(.2)
    # # k = cv2.waitkey(5) & 0xFF
    # if k ==27:
        # break
