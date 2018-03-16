import os

os.chdir(r'C:\Users\Assassin123\Desktop')
for i in os.listdir('.'):
    if i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png') \
       or i.endswith('.PNG') or i.endswith('.gif') or i.endswith('.JPG')\
       or i.endswith('.JPEG'):
        os.remove(os.path.join('.',i))
        
