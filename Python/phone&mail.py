#! python3
#this script filters out all phone numbers and mail ids from the text in
#clipboard and pastes the numbers and ids back to the clipboard.

import re, pyperclip

text=pyperclip.paste()

regexObj=re.compile(r'([ ,\.]\d{10}[ ,.]|[a-zA-z0-9]+@[a-z]+\.com)+')
matches=regexObj.findall(text)
newtext='\n '.join(matches)
pyperclip.copy(newtext)

input()
