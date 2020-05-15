import cv2
import numpy as np

drawing = False
ix, iy = -1, -1

def draw_circle(event, x, y, flags, params):
	global ix, iy, drawing, mode

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(winname = 'my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)

while True:
	cv2.imshow('my_drawing', img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
	elif k == 27:
		break
cv2.destroyAllWindows()