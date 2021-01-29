import face_recognition
import numpy as np
from PIL import Image
import cv2

image = face_recognition.load_image_file('me1.png')
for f in face_recognition.face_locations(image):
    top,right,bottom,left = f
    face_img = image[top:bottom, left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.show()
    cv2.imshow('frame', pil_img)