from time import sleep
from win32.win32api import GetCursorPos, GetKeyState
from pynput.keyboard import Listener

def keyIsUp(key):
    keystate = GetKeyState( key )
    if (keystate == 0) or (keystate == 1):
        return True
    else:
        return False
def keyIsDown(key):
    keystate = GetKeyState( key )
    if (keystate != 0) and (keystate != 1):
        return True
    else:
        return False

def on_press(key):
    print("Key pressed: {0}".format(key))
    aplus()

def on_release(key):
    print("Key released: {0}".format(key))

def initlistener():
    handler = Listener(on_press=on_press,on_release=on_release)
    handler.start()

def aplus():
    global a
    a+=1
    
if __name__ == "__main__":
    initlistener()
    a = 10
    while True:
        sleep(1)
        print(".",a)
        aplus()