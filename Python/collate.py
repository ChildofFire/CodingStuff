dic={
    'A':[

{

"name": "John",

"key2": "val2",

"key3": "val3",

"key4": "",

"key5": "",

"key6": ""

},

{

"name": "John",

"key2": "",

"key3": "",

"key4": "",

"key5": "val5",

"key6": "val6"

}

]
}

for i,j in dic.items():
    newdic=j[0]
    for k in range(1,len(j)):
        for m,n in j[k].items():
            if newdic[m]=="":
                newdic[m]=n
    dic[i]=newdic

print (dic)
'''dic3=lst[0]
for i in range(0,len(lst)):
    for j,k in lst[i].items():
        if dic3[j]=="":
            dic3[j]=k

print(dic3)
      '''      
