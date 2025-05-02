import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time
from collections import Counter
import pyautogui as at

base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

cap = cv2.VideoCapture(0)

gesture_list = []  # Liste, tanınan jestlerin kategorilerini depolamak için

start_time = time.time()  # Başlangıç zamanı

wintab = False

def control(gesture):
    if gesture == "altf4":
        at.hotkey('altleft', 'f4')

    elif gesture == "enter":
        at.press('enter')

    elif gesture == "sag":
        at.press('right')

    elif gesture == "sol":
        at.press('left')

    elif gesture == "sesac":
        for i in range(8):
            at.press('volumeup')

    elif gesture == "seskapa":
        for i in range(8):
            at.press('volumedown')

    elif gesture == "ss":
        at.press('printscreen')

    elif gesture == "wintab":
        if wintab == False:
            at.hotkey('win', 'tab')

    else:
        print("Geçersiz işlem girdiniz!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame from webcam.")
        break
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    recognition_result = recognizer.recognize(image)

    if recognition_result.gestures:
        top_gesture = recognition_result.gestures[0][0]
        gesture_list.append(top_gesture.category_name)  # Jest kategorisini listeye ekle

    cv2.imshow('Gesture Recognition', frame)

    # 1 saniye geçtiğinde işlemleri tamamla
    if time.time() - start_time >= 1:
        # Liste boş değilse en çok geçen elemanı bul
        if gesture_list:
            most_common_gesture = Counter(gesture_list).most_common(1)[0][0]
            control(most_common_gesture)
            if most_common_gesture == "wintab":
                wintab = True
            elif most_common_gesture == "enter":
                wintab = False
        
        # Listeyi temizle ve zamanı sıfırla
        gesture_list.clear()
        start_time = time.time()

    # q tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
