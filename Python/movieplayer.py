#! python3
#plays a random movie from the D: drive.

import os,random

ep_names=[]

for dirpath, dirnames, filenames in os.walk('D:'):
   for i in filenames:
       if not (i.lower().endswith('.srt') or i.lower().endswith('.zip')\
               or i.lower().endswith('.ifo') or i.lower().endswith('.nfo')):
           ep_names.append(os.path.join(dirpath,i))

os.startfile(random.choice(ep_names))

os.startfile(r'C:\Users\Assassin123\Desktop\Python Scripts\Random.py')
