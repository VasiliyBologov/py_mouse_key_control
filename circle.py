def circle():
    time.sleep(2)
    x0, y0 = pyautogui.position()
    r = 100
    while True:
        u = 6.3
        while u > 0:
            x1 = x0 + r * math.cos(u)
            y1 = y0 + r * math.sin(u)
            print(int(x1), int(y1), u)
            pyautogui.moveTo(int(x1), int(y1), duration=0)
            u -= 0.1
        pyautogui.click(pyautogui.position())
        time.sleep(20)
