#https://www.hackerrank.com/challenges/closest-numbers/problem
input()
array=[int(x) for x in input().split()]
array.sort()
mindiff=abs(array[0]-array[1])
closest=[]
for i in range(1,len(array)-1):
	diff=abs(array[i]-array[i+1])
	if mindiff>=diff:
		if mindiff>diff:
			mindiff=diff
			closest=[array[i],array[i+1]]
		else:
			closest+=[array[i],array[i+1]]

print(' '.join([str(x) for x in closest]))