import cv2
from cv2 import VideoCapture
from cv2 import waitKey
import pyautogui   
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)    #flip frame on y axis (0 is use for x axis)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks     #working on the basis of landmarks on hands
    if hands:         #around 21 landmarks on our hand
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:           #for index finger
                    cv2.circle(img = frame, center = (x,y), radius = 20, color = (0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:           #for thumb
                    cv2.circle(img = frame, center = (x,y), radius = 20, color = (0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 40:     #initiates a click when difference between the thumb and index finger becomes less then 40
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
