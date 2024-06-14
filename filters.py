import cv2
path = r"C:\Users\ZAID\Videos\animal.mp4"
camera = cv2.VideoCapture(path) # address of the video file
while camera.isOpened():
    state, frame = camera.read()
    if not state:
        print('frame skipped')
        continue
    # filters
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # cv2.imshow('camera 1', frame)
    # cv2.imshow('gray out', gray)
    # cv2.imshow('rgb out', rgb)
    # make the gray frame 3D for stacking purpose
    gray3d = cv2.merge([gray, gray, gray])
    # stack all 3 together vertical
    stacked_frame = cv2.vconcat([frame, rgb, gray3d])
    # resize by half
    stacked_frame = cv2.resize(stacked_frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow('stacked frame window', stacked_frame)
    if cv2.waitKey(10) == ord('q'):
        print("Video closing")
        break
camera.release()
cv2.destroyAllWindows()