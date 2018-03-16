#! python3
#this program takes a string of space separated ints present in the clipboard,
#finds their sum and prints it.

import pyperclip

text=pyperclip.paste()
arr=text.split(' ')
summ=0
for i in arr:
    summ+=int(i)

print(summ)
