import cv2

camera = cv2.VideoCapture(0) # index 0 is the default camera
while camera.isOpened():
    state, frame = camera.read()
    if not state:
        print('Camera is not working')
        break
    # implement your logic here
    cv2.imshow('camera 1', frame)
    if cv2.waitKey(1) == ord('q'):
        print("Camera closing")
        break
camera.release()
cv2.destroyAllWindows()