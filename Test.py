import pyautogui

stage_started = True
mission_started = True
correct_windows = True
afkbot = True
missioncount = 0

while stage_started and mission_started and afkbot:
    click= pyautogui.locateCenterOnScreen("Image\Stage_startb.png", confidence = 0.5)
