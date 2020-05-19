import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'MPEG')
writer = cv2.VideoWriter('myFace.avi', fourcc, 20.0, (640,480))

while True:

  ret, frame = cap.read()
  writer.write(frame)

  cv2.imshow('frame', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
writer.release()
cv2.destroyAllWindows()