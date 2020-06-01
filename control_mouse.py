import pyautogui
import sys

def get_position():
    while True:
        #print(pyautogui.position())
        sys.stdout.write("\rmouse position {}".format(pyautogui.position()))



if __name__ == '__main__':
    get_position()