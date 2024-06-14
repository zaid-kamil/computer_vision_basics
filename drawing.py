import cv2
from datetime import datetime 

camera = cv2.VideoCapture(0) # index 0 is the default camera
while camera.isOpened():
    state, frame = camera.read()
    if not state:
        print('Camera is not working')
        break
    h, w, _ = frame.shape
    print(f'Height: {h}, Width: {w}')
    tc, bc = (0,0), (w, 50)
    cv2.rectangle(frame, tc, bc, (255,255,255), -1)
    msg = 'webcam 1 recording...'
    cv2.putText(frame, msg, (20, 30), 
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cv2.putText(frame, date, (w-260, 30), 
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,100,0), 1)
    cv2.circle(frame, (w//2, h//2), 50, (0,255,0), 2)
    
    cv2.imshow('camera 1', frame)
    if cv2.waitKey(1) == ord('q'):
        print("Camera closing")
        break
camera.release()
cv2.destroyAllWindows()