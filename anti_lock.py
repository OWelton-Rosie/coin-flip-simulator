import pyautogui
import time

def nudge_mouse(interval=30):
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y)
        time.sleep(0.1)
        pyautogui.moveTo(x, y)
        time.sleep(interval)
