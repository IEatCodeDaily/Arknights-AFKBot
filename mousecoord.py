import pyautogui
import time
from random import random

def randomfloat(min,max):
    return min + random()*(max - min)

while(True):
    pyautogui.displayMousePosition()