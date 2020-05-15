import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)


img = cv2.imread("/home/dharana/Desktop/OpenCV/Computer-Vision-with-Python/DATA/dog_backpack.jpg")
cv2.namedWindow(winname='dog')
cv2.setMouseCallback('dog',draw_circle)

while True:
	cv2.imshow('dog', img)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()