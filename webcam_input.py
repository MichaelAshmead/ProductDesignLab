import cv2

import numpy as np
import landmarks

SCALE_FACTOR = 2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(-1)
vc.set(3,500)
vc.set(4,500)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    s = landmarks.get_landmarks(frame)

    if s is not None:
        # Check if 37 is getting too close to 41
        left_eye_bottom = s[list(range(42, 48))][1].tolist()[0][1]
        #print(left_eye_bottom)
        left_eye_top = s[list(range(42, 48))][5].tolist()[0][1]
        #print(left_eye_top)
        if left_eye_top - left_eye_bottom <= 6:
            print("Eyes closed " + str(left_eye_top) + " " + str(left_eye_bottom))
        else:
            print("Eyes open " + str(left_eye_top) + " " + str(left_eye_bottom))

        frame = landmarks.annotate_landmarks(frame, s)

    # resize image
    frame = cv2.resize(frame, (frame.shape[1] * SCALE_FACTOR,
                               frame.shape[0] * SCALE_FACTOR))

    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(1) # frame is shown for minimal time possible

    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
