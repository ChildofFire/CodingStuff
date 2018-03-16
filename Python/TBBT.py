#! python3
#plays a random episode of the big bang theory

import os,random

ep_names=[]

for dirpath, dirnames, filenames in os.walk(r'E:\Big Bang theory'):
   for i in filenames:
       if not (i.lower().endswith('.srt') or\
               i.lower().endswith('.zip') or\
               i.lower().endswith('.ifo') or\
               i.lower().endswith('.nfo')):
           ep_names.append(os.path.join(dirpath,i))

os.startfile(random.choice(ep_names))
