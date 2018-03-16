from sys import *
def countchar(s):
    dic={}
    for i in s:
        dic.setdefault(i,0) #initializes the value of a new key in the dict to 0. If key already present, does not change the existing value.
        dic[i]+=1
    return dic

t=int(input())
while(t>0):
    s=input()
    d=sorted(countchar(s).items())
    print(d)
    t-=1

input()
