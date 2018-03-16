#! python3
#renames all files with american date format into indian date format

import os, re, shutil

os.chdir(r'C:\Users\Assassin123\Desktop\Test')

regexobj=re.compile(r'(.*)(0[1-9]|1[0-2])-([0-2][0-9]|3[01])-(20\d{2})(.*)')

for filename in os.listdir():
    match=regexobj.search(filename)
    if match:
        before=match.group(1)
        month=match.group(2)
        day=match.group(3)
        year=match.group(4)
        after=match.group(5)
        newname=before+day+'-'+month+'-'+year+after
        shutil.move(filename,newname)
    else:
        print('''file name: "'''+filename+'''" don't contain date or is already in indian format''')
