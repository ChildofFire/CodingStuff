import os, shelve

os.chdir(r'C:\Users\Assassin123\Desktop\Test') #use os.makedirs(dirName) if directory doesnt exist

'''fileObj=open(r'Test.txt','a')
fileObj.write(r'Hey there.. This is a test file created by my first file handling Python script')
fileObj.close()
file=open(r'Test\Test.txt','r')
string=file.read()
print(string)
'''
shelfFile=shelve.open('shelfFile')
friends=['Somesh', 'A.p', 'Soham', 'Baba', 'Jindal']
shelfFile['friends']=friends #saves the variable friends's value as an entry in the
#shelf file 'shelfFile'. Now this value can be retrieved in any program at any time.
shelfFile.close()
#test this functionality (retrieval of the value of 'friends') by running a different
#test script: shelves.py

shelfFile=shelve.open('shelfFile')
'''print(shelfFile['friends'])
print(shelfFile['useless'])
print(shelfFile['number'])
print(shelfFile['float'])
'''
#variables saved from shelves.py script
for i,j in shelfFile.items():
    print(i,': ',j)
