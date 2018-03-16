#! python3
#saves variable values in a different .py file (saver.py) instead of a shelve
#file

import pprint

myDict={'Friends': ['AP','Soham','Baba'], 'Likes':['Math','Programming'],\
        'languages':['C++','Python','Java']}
myInt=123
myFloat=12.3333
myName='Somesh Thakur'

fileobj=open(r'saver.py','w')
fileobj.write('myDict='+pprint.pformat(myDict)+'\nmyInt='+pprint.pformat(myInt)\
              + '\nmyFloat='+pprint.pformat(myFloat)+'\nmyName='+\
              pprint.pformat(myName))
fileobj.close()
