from win32 import win32gui
import pywinauto

open_windows = [[]]

#print(active, win32gui.GetWindowText(active))
def getactive():
    win32gui.GetForegroundWindow()

def getprocess(hwnd, var):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowTextLength(hwnd) != 0:
            open_windows.append([hwnd,win32gui.GetWindowText(hwnd)])


win32gui.EnumWindows(getprocess, None)
print(open_windows)
print(win32gui.GetForegroundWindow())