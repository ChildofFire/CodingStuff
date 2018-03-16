import sys

def fibonacci(n):
    a,b,c=0,1,0
    while c<n:
        yield a
        a,b=b,b+a
        c+=1

f=fibonacci(5)
it=iter(f)
for i in it:
    print(i,end=' ')

input()
