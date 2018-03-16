array=[int(i) for i in input().split()]
counter=[0]*10
for i in array:
	counter[i]+=1
medianpos=len(array)//2+1 if len(array)%2 else len(array)//2
count=0
i=0
while count<medianpos:
	count+=counter[i]
	i+=1
