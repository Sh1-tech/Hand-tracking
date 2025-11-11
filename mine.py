import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

while True:
    success, frame = camera.read() 
    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(RGB_frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                print(hand_landmarks)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
        cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()