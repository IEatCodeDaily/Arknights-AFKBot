import pyautogui
from time import sleep
import getprocess
import pynput.keyboard as keyboard

#Variables declaration
images = ["Image/Stage_startb2.png","Image/Mission_startb.png","Image/Stage_finish.png", "Image/pause_button.png", "Image/levelup.png"]
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
    global afkbot
    if key == keyboard.Key.end:
        afkbot = False
    if key == keyboard.Key.home:
        afkbot = True
    sleep(.1)

def initlistener():
    handler = keyboard.Listener(on_press=on_press)
    handler.start()

def main():
    global stage_started, mission_started, missioncount
    count = 0
    print("\rChecking for %s" %images[0])
    while stage_started == 0 and afkbot:
        try:
            clickx, clicky = pyautogui.locateCenterOnScreen(images[0], confidence = 0.9)
        except TypeError:
            #print("\r%s not found. Retrying..." %images[1])
            print(".")
            clickpos = pyautogui.locateCenterOnScreen(images[2], confidence = 0.6)
            if clickpos != None:
                pyautogui.click(clickpos)
        else:
            print("Image found. Stage started")
            pyautogui.click(clickx, clicky)
            stage_started = True

    print("\rChecking for %s" %images[1])
    while stage_started and mission_started == 0 and afkbot:
        try:
            clickx, clicky = pyautogui.locateCenterOnScreen(images[1], confidence = 0.9)
        except TypeError:
            #print("\r%s not found. Retrying..." %images[1])
            print(".")
            clickpos = pyautogui.locateCenterOnScreen(images[0], confidence = 0.9)
            if clickpos != None:
                pyautogui.click(clickpos)
        else:
            print("Image found. Mission started")
            pyautogui.click(clickx, clicky)
            mission_started = True
    print("Checking for result screen")
    while stage_started and mission_started and afkbot:
        try:
            clickx, clicky = pyautogui.locateCenterOnScreen(images[2], confidence = 0.5)
            sleep(2)
        except TypeError:
            print(".")
            levelup = pyautogui.locateCenterOnScreen(images[4], confidence = 0.9)
            if levelup != None:
                pyautogui.click(levelup)
        else:
            pyautogui.click(clickx,clicky)
            missioncount+=1
            stage_started = False
            mission_started = False
            print("Stage completed. Restarting loop")
            print("Mission Finished:", missioncount)    

def main2():
    global stage_started, mission_started, missioncount
    count = 0
    print("\rChecking for %s" %images[0])
    clickpos = pyautogui.locateCenterOnScreen(images[0], confidence = 0.9)
    sleep(1)
    if clickpos != None:
        print("Image found. Stage started")
        pyautogui.click(clickpos)
    else:
        print("\rChecking for %s" %images[1])
        clickpos = pyautogui.locateCenterOnScreen(images[1], confidence = 0.9)
        sleep(1)

        if clickpos != None:
            print("Image found. Mission started")
            pyautogui.click(clickpos)
        else:
            print("Checking for result screen")
            clickpos = pyautogui.locateCenterOnScreen(images[2], confidence = 0.6)
            sleep(1)

            if clickpos != None:
                pyautogui.click(clickpos)
                print("Stage completed. Restarting loop")
                print("Mission Finished:", missioncount)
            else:
                pass

if __name__ == "__main__":
    initlistener()
    while True:
        while afkbot and correct_windows:
            
            main()

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