import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(-1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    print type(frame)
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(25) # frame is shown for 25 ms
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
