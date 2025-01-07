import time

import cv2

video_path = 'bird_short.mp4'  
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Failed to load video.")
    exit()

frame_count = 0
print("start after 20 seconds sleep")
print("Press 'q' to finish")
while True:
    ret, frame = cap.read()

    if not ret:
        break
    

    cv2.imshow('Video Playback', frame)

    # finish to press 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    if frame_count == 0:
        time.sleep(20)

    frame_count += 1
cap.release()
cv2.destroyAllWindows()
