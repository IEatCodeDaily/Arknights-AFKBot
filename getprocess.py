from win32 import win32gui
import pywinauto


#print(active, win32gui.GetWindowText(active))
def checkActiveWindow(CorrectWindow):
    if CorrectWindow == win32gui.GetForegroundWindow():
        return True
    else:
        return False

def getOpenWindows():
#Return an array of visible windows PID and Name
    open_windows = []
    def enum_handler(hwnd, args):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowTextLength(hwnd) != 0:
            open_windows.append([hwnd, win32gui.GetWindowText(hwnd)])
    win32gui.EnumWindows(enum_handler, None)
    return open_windows
