import os,shutil
os.chdir('C:\\Users\\Assassin123\\Desktop')
for i in os.listdir('.'):
	if i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png') \
       or i.endswith('.PNG') or i.endswith('.gif') or i.endswith('.JPG')\
       or i.endswith('.JPEG') or i.endswith('.mp4') or i.endswith('.MP4'):
       		shutil.move(i,os.path.join('C:\\Users\\Assassin123\\Downloads\\Programs\\pop\\',i))
