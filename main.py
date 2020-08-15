import pyautogui
import time
from random import random

def randomfloat(min,max):
    return min + random()*(max - min)


images = ["Image/Stage_startb.png","Image/Mission_start.png","Image/Stage_finish.png"]
count = 0
stage_started = 0
mission_started = 0
mission_finished = 0

while True:
    print("\rChecking for %s" %images[0])
    while stage_started == 0:
        try:
            count += 1
            if count == 3:
                pyautogui.click(1700,300)
                count = 0
            clickx, clicky = pyautogui.locateCenterOnScreen(images[0])
        except TypeError:
            print("\r%s not found. Retrying..." %images[0])
        else:
            print("Image found. Stage started")
            pyautogui.click(clickx, clicky)
            stage_started = 1
            mission_started = 0

    print("\rChecking for %s" %images[1])
    while stage_started == 1 and mission_started == 0:
        try:
            clickx, clicky = pyautogui.locateCenterOnScreen(images[1])
        except TypeError:
            print("\r%s not found. Retrying..." %images[1])
        else:
            print("Image found. Mission started")
            pyautogui.click(clickx, clicky)
            stage_started = 0
            mission_finished += 1
            mission_started = 1
    print("Mission finished:", mission_finished)

            
#    for i in images:
#        try:
#            print("Checking for %s" %i)
#            clickx, clicky = pyautogui.locateCenterOnScreen(i)
#        except TypeError:
#            print("checking for the next image")
#        else:
#            print("Image found")
#            pyautogui.click(clickx, clicky)
#    if count == 5:
#        pyautogui.click(1700,300)
#    count+=1
#    pyautogui.sleep(.5)