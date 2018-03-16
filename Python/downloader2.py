#! python3

import requests, bs4,os

os.makedirs(r'C:\Users\Assassin123\Downloads\Programs\pop\MonsterSex',exist_ok=True)
os.chdir(r'C:\Users\Assassin123\Downloads\Programs\pop\MonsterSex')

url='http://www.porncomix.info/doll-2/00-62/'
count=1

while count<32:
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)
    image=soup.select('.attachment-image a')
    imgurl=image[0].get('href')
    res=requests.get(imgurl)
    imagefile=open('The Doll'+str(count)+'.jpg','wb')
    for i in res.iter_content(100000):
        imagefile.write(i)
    imagefile.close()
    nextlink=soup.select('.next-link a')
    url=nextlink[0].get('href')
    count+=1

    
