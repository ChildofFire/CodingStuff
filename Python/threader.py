#! python3
# creates two threads in the program

import threading, time, webbrowser

def wait(name):
    time.sleep(5)
    print('facebook is starting '+name+'...')
    webbrowser.open(r'https://www.facebook.com')

threadObj=threading.Thread(target=wait, args=['somesh'])
threadObj.start()
print('facebook will open in 5 seconds.')
