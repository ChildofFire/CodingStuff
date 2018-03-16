import shelve, os

os.chdir(r'C:\Users\Assassin123\Desktop\Test')
sf=shelve.open('shelfFile')
f=sf['friends']
print(f)
foo='just another useless variable'
num=12
floater=12.3333
sf['useless']=foo
sf['number']=num
sf['float']=floater
sf.close()
