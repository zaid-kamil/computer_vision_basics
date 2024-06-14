import cv2
path = r"C:\Users\ZAID\Videos\animal.mp4"
camera = cv2.VideoCapture(path) # address of the video file
# add 3 trackbars for ksizeX, ksizeY, sigmaX
win_name = 'camera 1'
cv2.namedWindow(win_name)
track_ksizeX = cv2.createTrackbar('ksizeX', win_name, 0, 100, lambda v: print(v))
track_ksizeY = cv2.createTrackbar('ksizeY', win_name, 0, 100, lambda v: print(v))
track_sigmaX = cv2.createTrackbar('sigmaX', win_name, 0, 100, lambda v: print(v))
while camera.isOpened():
    state, frame = camera.read()
    if not state:
        print('frame skipped')
        continue
    ksx = cv2.getTrackbarPos('ksizeX', win_name)
    ksy = cv2.getTrackbarPos('ksizeY', win_name)
    sig = cv2.getTrackbarPos('sigmaX', win_name)
    try:
        result = cv2.GaussianBlur(frame, (ksx, ksy), sig)
        cv2.imshow(win_name, result)
    except Exception as e:
        print(e)
    if cv2.waitKey(10) == ord('q'):
        print("Video closing")
        break
camera.release()
cv2.destroyAllWindows()