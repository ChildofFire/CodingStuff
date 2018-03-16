#! python3
#plays a random episode of the big bang theory from any season 1 through 8.

import os,random

ep_names=[]

for dirpath, dirnames, filenames in os.walk(r'E:\Big Bang Theory'):
   for i in filenames:
       if i.endswith('.mp4'):
           ep_names.append(os.path.join(dirpath,i))

os.startfile(random.choice(ep_names))
