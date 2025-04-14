# 🛡️ HandGuard - AI-Powered Gesture-Based Alarm System

**HandGuard** is a real-time computer vision system designed to detect specific hand gestures (like a help signal) through CCTV or webcam footage. When such a gesture is identified, it automatically triggers an alarm and can be extended to notify nearby authorities or emergency services with the exact location.

---

## 🚨 Use Case

This system is ideal for **public safety monitoring** in:

- **CCTVs at public spaces** (e.g. metro stations, parks, campuses)
- **ATMs, parking lots, or elevators**
- **Smart homes or offices**
- Any space where discreet emergency signals may be necessary

HandGuard enables people to **ask for help silently**, without needing to speak, press buttons, or trigger physical alarms manually.

---

## ✨ Features

- 🖐️ Detects custom hand gestures (like the "help me" sign)
- ⏰ Triggers an immediate alarm or alert
- 📍 Can integrate with GPS/location APIs to report the incident location
- 🧠 Powered by AI/ML models trained to recognize real-time gestures
- ⚙️ Lightweight and works with standard CCTV or webcam feeds

---

## 📦 Tech Stack

- **Python**
- **OpenCV**
- **MediaPipe / TensorFlow / Custom ML Model**
- Optional: **Flask / FastAPI** for backend alert handling
- Optional: **Twilio / Telegram API / Email** for notifications

---

## 🛠️ How It Works

1. Camera captures real-time video stream.
2. AI model scans each frame for a specific hand gesture.
3. Upon detection:
   - An alarm rings (local or connected system)
   - Emergency contacts (e.g., police) are notified with time and location
4. System resets after a cooldown period or manual intervention.

---

## 📍 Future Integrations

- GPS mapping of the incident area
- Live dashboard for emergency response centers
- Integration with government emergency networks
- Multi-gesture support (for different types of alerts)

---

## 🚀 Getting Started

```bash
git clone https://github.com/SuhaniChaturvedi/HandGuard.git
cd HandGuard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
