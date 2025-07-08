# 🎨✋ Virtual marker using Hand Tracking (MediaPipe + OpenCV)

This project implements a **virtual marker application** that uses your hand gestures (tracked via MediaPipe) to select colors and draw on a virtual canvas in real-time.

---

## 📂 Files

### ✅ `Virtualmarker.py`

- Main application that:
  - Loads header images (color buttons) from `Header` folder.
  - Uses webcam to track your hand.
  - Lets you choose brush colors using finger gestures.
  - Supports **drawing mode** and **selection mode**.
  - Uses a canvas to retain drawn content.

### ✅ `HandTrackingModule.py`

- Contains `handDetector` class.
- Modular hand tracking helper used in the main painter script.
- Features:
  - Detect hands and landmarks.
  - Get landmark positions (`findPosition()`).
  - Check which fingers are up (`fingerUps()`).

---

## 🚀 Features

- Real-time detection of **21 hand landmarks**.
- Select different brush colors using your index and middle fingers ("Selection mode").
- Draw using index finger ("Drawing mode").
- Supports eraser.
- Overlays custom header images for color selection.
- Separate canvas layer to avoid overwriting webcam feed.

---

## ⚙️ Installation

```bash
pip install opencv-python mediapipe numpy
