#downloads the bing image of the day and sets it as background

import bs4, requests, ctypes, datetime,sys

res=requests.get(r'https://bingwallpaper.com')

res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,"html.parser")

bingdate=soup.select('.cursor_zoom')[0].get('href').split('.')[0] #extracts bing image timestamp in YYYYMMDD format.

#if the timestamp on the image is less than that of now, program exits.
currdate=datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d") #string of current date in YYYYMMDD format

if currdate > bingdate:
        sys.exit()

#else continue
imageurl=soup.select('.cursor_zoom img')[0].get('src')
imagename=soup.select('.cursor_zoom img')[0].get('alt').split('(')[0].strip() #gets the
#imagename without parentheses and special characters.
res=requests.get(imageurl)
imagefile=open(r'C:\Users\Assassin123\Desktop\Bing\%s.jpg'%imagename,'wb')
for j in res.iter_content(100000):
        imagefile.write(j)
imagefile.close()


imagepath=r'C:\Users\Assassin123\Desktop\Bing\%s.jpg'%imagename
SPI_SETDESKWALLPAPER=20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagepath,3)
