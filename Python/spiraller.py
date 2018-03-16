#draws a square spiral in paint

import pyautogui
import time

time.sleep(5) #to allow time to move cursor into the canvas
pyautogui.doubleClick(337,102)  #selects the brush menu
time.sleep(1)
pyautogui.click(329,131)        #selects std. brush
pyautogui.click(200,265)        #clicks in canvas

distance=200

while distance>0:
    pyautogui.dragRel(distance,0)
    distance-=5
    pyautogui.dragRel(0,distance)
    pyautogui.dragRel(-distance,0)
    distance-=5
    pyautogui.dragRel(0,-distance)
    x,y=pyautogui.position()

pyautogui.click(242,100)    #clicks on the eraser
pyautogui.click(x,y)        #clicks at the center of the spiral
distance=5
while distance<201:
    pyautogui.dragRel(distance,0)
    pyautogui.dragRel(0,-distance)
    distance+=5
    pyautogui.dragRel(-distance,0)
    pyautogui.dragRel(0,distance)
    distance+=5
