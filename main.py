import pyautogui
from time import sleep
import getprocess
import kbhit
import pynput.keyboard as keyboard

#Variables declaration
images = ["Image/Stage_startb2.png","Image/Mission_startb.png","Image/Stage_finish.png"]
stage_started = False
mission_started = False
missioncount = 0
correct_windows = True
afkbot = True

def resetvalue():
    global stage_started, mission_started, missioncount, afkbot
    stage_started = False
    mission_started = False
    correct_windows = True
    afkbot = True

def botstop():
    global afkbot
    afkbot = False

def on_press(key):
    if key == keyboard.Key.end:
        botstop()
    if key == keyboard.Key.home:
        resetvalue()
    sleep(.1)

def initlistener():
    handler = keyboard.Listener(on_press=on_press)
    handler.start()

def main():
    global stage_started, mission_started, missioncount
    count = 0
    while correct_windows and afkbot:
        print("\rChecking for %s" %images[0])
        while stage_started == 0 and afkbot:
            try:
                count += 1
                if count == 3:
                    pyautogui.click(1700,300)
                    count = 0
                clickx, clicky = pyautogui.locateCenterOnScreen(images[0], confidence = 0.9)
            except TypeError:
                #print("\r%s not found. Retrying..." %images[1])
                print(".")
            else:
                print("Image found. Stage started")
                pyautogui.click(clickx, clicky)
                stage_started = 1
                mission_started = 0

        print("\rChecking for %s" %images[1])
        while stage_started and mission_started == 0 and afkbot:
            try:
                clickx, clicky = pyautogui.locateCenterOnScreen(images[1], confidence = 0.9)
            except TypeError:
                #print("\r%s not found. Retrying..." %images[1])
                print(".")
            else:
                print("Image found. Mission started")
                pyautogui.click(clickx, clicky)
                stage_started = 0
                missioncount += 1
                mission_started = 1


if __name__ == "__main__":
    initlistener()
    while True:
        while afkbot:
            main()
            print("Mission finished:", missioncount)

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