#! python3
#searches for a user specified regex in all .txt files of test folder
#and displays lines that have a match.

import re, sys, os

regexobj=re.compile(sys.argv[1])

os.chdir(r'C:\Users\Assassin123\Desktop\Test')

for i in os.listdir():
    if i.endswith('.txt'):
        file=open(i,'r')
        for line in file:
            if regexobj.search(line):
                print(line)
        file.close()
input()
