import cv2

camera = cv2.VideoCapture(0) # index of camera
bgmask = cv2.createBackgroundSubtractorKNN()
while camera.isOpened():
    state, frame = camera.read()
    if not state:
        print('camera not available')
        break
    fg = bgmask.apply(frame)
    cv2.imshow('camera 1', frame)
    cv2.imshow('fg', fg)
    if cv2.waitKey(10) == ord('q'):
        print("Video stopped")
        break
camera.release()
cv2.destroyAllWindows()