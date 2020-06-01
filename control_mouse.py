import pyautogui
import sys

def get_position():
    while True:
        #print(pyautogui.position())
        x, y = pyautogui.position()
        sys.stdout.write("\rmouse position x = {} y = {}".format(x, y))



if __name__ == '__main__':
    get_position()