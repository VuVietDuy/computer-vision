import cv2
import os

def cap_video():
    i = 0
    video = cv2.VideoCapture(0)
    if not os.path.exists('duy'):
        os.makedirs('duy')
    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break
        cv2.imshow('Video', frame)
        key = cv2.waitKey(1) & 0xFF  # Wait for keypress
        if key == ord('a'):
            cv2.imwrite(os.path.join('duy', f"{i}.png"), frame)
            i += 1
        elif key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

cap_video()