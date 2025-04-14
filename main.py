import cv2
import mediapipe as mp
import pygame
import time
import os
import requests
from telegram import Bot

# ====================== TELEGRAM ALERT CONFIG ======================
BOT_TOKEN = '7898323484:AAEWJHTQutwxhqTy7sCOaINXzXvssjxNnqk'       # 🔒 Replace with your bot token
CHAT_ID = '1475279755'           # 🔒 Replace with your chat ID

def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return f"📍 Location: {data['city']}, {data['region']}, {data['country']} (Approx)"
    except:
        return "📍 Location not available"

def send_telegram_alert():
    bot = Bot(token=BOT_TOKEN)
    location = get_location()
    message = f"🚨 Emergency Alert! Help gesture detected.\n{location}"
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print("✅ Telegram alert sent!")
    except Exception as e:
        print("❌ Failed to send Telegram alert:", e)

# ===================== HAND DETECTION SETUP ========================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

alarm_triggered = False
last_trigger_time = 0
alarm_path = os.path.join(os.path.dirname(__file__), "alarm.wav")
pygame.mixer.init()

def is_last_two_fingers_up(landmarks):
    fingers = {
        "index": landmarks[8].y < landmarks[6].y,
        "middle": landmarks[12].y < landmarks[10].y,
        "ring": landmarks[16].y < landmarks[14].y,
        "pinky": landmarks[20].y < landmarks[18].y,
    }
    return (
        not fingers["index"] and
        not fingers["middle"] and
        fingers["ring"] and
        fingers["pinky"]
    )

# ========================== MAIN LOOP ==============================
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            if is_last_two_fingers_up(handLms.landmark):
                current_time = time.time()
                if not alarm_triggered or (current_time - last_trigger_time > 5):
                    print("🚨 Gesture Detected! Triggering Alarm and Alert...")
                    try:
                        pygame.mixer.music.load(alarm_path)
                        pygame.mixer.music.play()
                    except Exception as e:
                        print("⚠️ Error playing alarm:", e)
                    send_telegram_alert()
                    alarm_triggered = True
                    last_trigger_time = current_time

    cv2.imshow("Hand Guard - Emergency Gesture Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
