import cv2

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

x = int(width // 2)
y = int(height // 2)

w = int(width // 4)
h = int(height // 4)

while True:
	ret, frame = cap.read()
	cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=4)
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()