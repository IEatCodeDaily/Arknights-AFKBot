import pyautogui
import random

def randomfloat(min,max):
    return min + random()*(max - min)

def getmousepos():
    pyautogui.displayMousePosition()

