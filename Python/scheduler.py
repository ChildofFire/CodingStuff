#! python3
# opens facebook 1 minute after running the script

import webbrowser, datetime, time

time2minslater=datetime.datetime.now()+datetime.timedelta(minutes=1)

while datetime.datetime.now()<time2minslater:
    time.sleep(1)

webbrowser.open(r'https://www.facebook.com/')
