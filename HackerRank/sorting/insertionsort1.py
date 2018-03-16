#https://www.hackerrank.com/challenges/insertionsort1/problem
input()
array=[int(x) for x in input().split()]
last=array[-1]
count=0
for i in range(len(array)-2,-1,-1):
	if array[i]>last:
		array[i+1]=array[i]
		print(' '.join([str(x) for x in array]))
	else:
		array[i+1]=last
		count+=1
		break
if count:
	print(' '.join([str(x) for x in array]))
else:
	array[0]=last
	print(' '.join([str(x) for x in array]))