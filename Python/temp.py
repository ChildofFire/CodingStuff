#removes all temporary files and folders and creates an empty Temp folder if it gets deleted.

import os , shutil, time
size=0
for dirpath, dirnames, filenames in os.walk(r"C:\Users\ASSASS~1\AppData\Local\Temp"):
    for names in filenames:
        try:
            size+=os.path.getsize(os.path.join(dirpath,names))
        except OSError:
            pass
    for names in dirnames:
        try:
            size+=os.path.getsize(os.path.join(dirpath,names))
        except OSError:
            pass

shutil.rmtree(r"C:\Users\ASSASS~1\AppData\Local\Temp", ignore_errors=True)
os.makedirs(r"C:\Users\ASSASS~1\AppData\Local\Temp",exist_ok=True)
if size<1024:
    string='bytes'
elif size>=1024 and size<(1024**2):
    size/=1024
    string='KB'
elif size>=(1024**2) and size<(1024**3):
    size/=(1024**2)
    string='MB'
else:
    size/=(1024**3)
    string='GB'
print(size,"%s of temp files deleted"%string)
input("Press RETURN to continue: ")
