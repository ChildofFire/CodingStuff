#! python3
#opens 2 new tabs for any google query passed as a comm. line. arg

import sys, requests, webbrowser, bs4

requestObj=requests.get('http://www.google.com/search?q='+' '.join(sys.argv[1:]))

requestObj.raise_for_status()

soupObj=bs4.BeautifulSoup(requestObj.text)

links=soupObj.select('.r a')

tabs=min(2,len(links))

print('href values\n')
for i in range(tabs):
    print(links[i].get('href')) #prints the href values from the selected <a> tags
    print()
    webbrowser.open('http://google.com'+links[i].get('href'))

input()
