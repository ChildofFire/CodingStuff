#! python3
#script to calculate the size of any folder (desktop)
import os

size=0

for dirpath, dirnames, filenames in os.walk(r'C:\Users\Assassin123\Desktop'):
    for directories in dirnames:
        size+=os.path.getsize(os.path.join(dirpath,directories))
    for files in filenames:
        size+=os.path.getsize(os.path.join(dirpath,files))

print ('size=',size/(1024*1024),'MB')
