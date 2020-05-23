import cv2
import numpy as np

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect_eye(img):
	face_img = img.copy()
	eye_rects = eye_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)
	
	for(x, y, w, h) in eye_rects:
		cv2.rectangle(face_img, (x, y), (x+w, y+h), (255, 255, 255), 10)
	
	return face_img

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read(0)
	frame = detect_eye(frame)
	cv2.imshow('Video Face Detect', frame)
	k = cv2.waitKey(1)

	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
