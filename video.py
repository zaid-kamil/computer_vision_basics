import cv2
path = r"C:\Users\ZAID\Videos\animal.mp4"
camera = cv2.VideoCapture(path) # address of the video file
while camera.isOpened():
    state, frame = camera.read()
    if not state:
        print('frame skipped')
        continue
    # implement your logic here
    cv2.imshow('camera 1', frame)
    if cv2.waitKey(10) == ord('q'):
        print("Video closing")
        break
camera.release()
cv2.destroyAllWindows()