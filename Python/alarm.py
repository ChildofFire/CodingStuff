#plays an alarm at the end of 5 minutes

import os, time

timeleft=300
while timeleft>0:
    print(timeleft)
    time.sleep(1)
    timeleft-=1

for i in range(3):
    os.startfile(r'C:\Users\Assassin123\Music\alarm.wav')
    time.sleep(4)
