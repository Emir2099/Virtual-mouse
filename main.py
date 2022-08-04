import cv2
from cv2 import VideoCapture
from cv2 import waitKey
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks     #working on the basis of landmarks on hands
    if hands:         #around 21 landmarks on our hand
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
