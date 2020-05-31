import pyautogui
import pydirectinput
import time

while(True):
    time.sleep(1)
    pyautogui.keyDown('q')
    time.sleep(.5)
    pyautogui.keyUp('q')