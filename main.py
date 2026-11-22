import time
import requests
import pyautogui

ESP32_URL = "http://192.168.4.1/mouse"

pyautogui.PAUSE = 0

print("Capsule Corpse mouse controller")
print("Starting...")

while True:
    try:
        response = requests.get(
            ESP32_URL,
            timeout=0.2,
            headers={"Cache-Control": "no-cache"}
        )

        if response.status_code == 200:
            data = response.text.strip()

            if "," in data:
                dx, dy = map(int, data.split(","))

                if dx != 0 or dy != 0:
                    pyautogui.moveRel(dx, dy)

    except Exception:
        pass

    time.sleep(0.01)
