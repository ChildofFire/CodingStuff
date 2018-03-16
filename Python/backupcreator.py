#! python3
#takes a zipfile backup of a folder (path specified through command line arg.)
#every time it is run and names successive backups as
#"<foldername>1.zip", "<foldername>2.zip", ...

import os, zipfile,sys

os.chdir(os.path.dirname(sys.argv[1]))

number=1
nummax=1
foldername=os.path.basename(sys.argv[1])
for i in os.listdir():
    if (os.path.isfile(foldername+'%s.zip'%nummax)):
        number=nummax+1
    nummax+=1

newZip=zipfile.ZipFile(foldername+'%s.zip'%number,'w',zipfile.ZIP_DEFLATED)
#ZIP_DEFLATED is the compression algo used.

for dirpath, dirnames , filenames in os.walk(foldername):
        print('Backing up '+dirpath+'...')
        newZip.write(dirpath)
        for filename in filenames:
            newZip.write(os.path.join(dirpath,filename))

newZip.close()
input("hit enter to close...")
