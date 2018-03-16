from copy import *
qualities={'Somesh':'Sarcastic','Soham':'Friendly','AP':'Funny'}

for i in qualities:
    print (i)
print(); print()
for i in qualities.keys():
    print(i)
print(); print()
for i in qualities.values():
    print(i)
print(); print()
for i in qualities.items():
    print(i)        
print(); print()

for i, j in qualities.items():
    print('name: '+i+', quality: '+j)

print('\n\n')

name=input("Name: ")
print(name+' is a '+qualities.get(name,'stranger')+' boy')

input()
