# Importing the required dependencies
import cv2  # for video rendering
import dlib  # for face and landmark detection
import imutils

# for calculating dist b/w the eye landmarks
from scipy.spatial import distance as dist

# to get the landmark ids of the left
# and right eyes ----you can do this
# manually too
from imutils import face_utils

cam = cv2.VideoCapture('assets/Video.mp4')


# Initializing the Models for Landmark and
# face Detection
detector = dlib.get_frontal_face_detector()
landmark_predict = dlib.shape_predictor(
    'Model/shape_predictor_68_face_landmarks.dat')

while 1:

    # If the video is finished then reset it
    # to the start
    if cam.get(cv2.CAP_PROP_POS_FRAMES) == cam.get(
            cv2.CAP_PROP_FRAME_COUNT):
        cam.set(cv2.CAP_PROP_POS_FRAMES, 0)

    else:
        _, frame = cam.read()
        frame = imutils.resize(frame, width=640)

        # converting frame to gray scale to pass
        # to detector
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detecting the faces---#
        faces = detector(img_gray)
        for face in faces:
            cv2.rectangle(frame, face[0], face[1],
                          (200, 0, 0), 1)

        cv2.imshow("Video", frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()
