#! python3
#zip file operations

import zipfile

zipfileobj=zipfile.ZipFile(r'C:\Users\Assassin123\Downloads\Compressed\glad.zip')
contents=zipfileobj.namelist()
print(contents)
for i in contents:
    if i.endswith('.h') or i.endswith('.c'):
        fileInfo=zipfileobj.getinfo(i)
        print('original size of '+i+' = '+str(fileInfo.file_size))
        print('after compression: '+str(fileInfo.compress_size))

zipfileobj.close()
