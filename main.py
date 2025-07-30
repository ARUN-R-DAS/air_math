import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hand = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

video = cv2.VideoCapture(0)
while True:
    success,frame = video.read()
    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand.process(frame_rgb)
    print(result)
    cv2.imshow("camFeed",frame)

    if cv2.waitKey(1) & 0xFF in [ord('q'),ord('Q')]:
        break

video.release()
cv2.destroyAllWindows()
