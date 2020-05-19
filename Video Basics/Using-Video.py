import cv2
import time

cap = cv2.VideoCapture('myFace.avi')

if cap.isOpened() == False:
	print('ERROR FILE NOT FOUND!')

while cap.isOpened():
	ret, frame = cap.read()
	
	if ret == True:
		
		time.sleep(1/20.0)
		cv2.imshow('frame', frame)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	else:
		break

cap.release()
cv2.destroyAllWindows()