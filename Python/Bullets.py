#! python3
'''copies text from the clipboard, adds an asterisk and space (Wikipedia way
to add a bullet) to each line and pastes it back to the clipboard.'''

import pyperclip

def addBullets(text):
    lines=text.split('\n')  #splits the text into different lines whenever a newline is encountered and stores the individual lines in a list named 'lines'
    
    for i in range(len(lines)):
        lines[i]='* '+lines[i]

    text2='\n'.join(lines)   #joins each individual line back into one text.
    return text2

pyperclip.copy(addBullets(pyperclip.paste()))

input()
