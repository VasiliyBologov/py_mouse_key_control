

import pyautogui
print(pyautogui.position())


pyautogui.moveRel(0, 50, duration=2)
pyautogui.moveRel(30, 50, duration=1)
pyautogui.moveRel(-50, 50, duration=3)
pyautogui.moveRel(150, 50, duration=0)
pyautogui.click(1200, 650)

pyautogui.scroll(200)

#pyautogui.typewrite("hello Geeks !")

pyautogui.hotkey("altleft", "tab")