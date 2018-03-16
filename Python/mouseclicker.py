#clicks mouse at specified position
import pyautogui

while True:
    x=int(input())
    y=int(input())
    pyautogui.doubleClick(x,y)
