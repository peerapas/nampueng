import cv2
import face_recognition
import numpy as np
from PIL import Image

capture = cv2.VideoCapture(0)
database_image = face_recognition.load_image_file('me1.png')
database_encodings = face_recognition.face_encodings(database_image, num_jitters = 2)[0]
known_face_encodings = [database_encodings]
known_face_names = ['Peerapas']

data_encoding = []
data_locations = []
data_names = []
img_counter = 0
frameProcess = True

while (True):
    ret, frame = capture.read()
    resizing = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
    rgb_resizing = resizing[:, :, ::-1]
    if frameProcess:
        data_locations = face_recognition.face_locations(rgb_resizing)
        data_encodings = face_recognition.face_encodings(rgb_resizing, data_locations, num_jitters = 1)
        data_names = []
        for dc in data_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, dc, tolerance = 0.44)
            print(matches)
            name = 'UNKNOWN'
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            data_names.append(name)
    frameProcess = not frameProcess
    for (top, right, bottom, left), name in zip(data_locations, data_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        break
    if k % 256 == 32:
        img_name = 'opencv_frame_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        print('{} is written'.format(img_name))
        img_counter += 1
capture.release()
cv2.destroyAllWindows()
    