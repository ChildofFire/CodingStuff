test=int(input())
while test>0:
    n=int(input())
    temp=input().split(' ')
    summ=0
    for i in temp:
        summ+=int(i)
    print(summ,end='\n')
    test-=1
