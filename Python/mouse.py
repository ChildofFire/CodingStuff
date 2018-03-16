#prints mouse position
import pyautogui

print('\n\n')

while True:
    x,y=pyautogui.position()
    posstr='X = '+str(x).rjust(4)+' Y = '+str(y).rjust(4)
    print(posstr,end='')
    print('\b'*len(posstr),end='',flush=True)
    
