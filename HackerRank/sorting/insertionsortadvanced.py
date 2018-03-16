#https://www.hackerrank.com/challenges/insertion-sort/problem

def countShifts(array):
	n=len(array)
	if n==1:
		return 0
	leftsize=n//2
	rightsize=n-leftsize
	lefthalf=array[:leftsize]
	righthalf=array[leftsize:]
	shifts=countShifts(lefthalf)+countShifts(righthalf)
	j,k=0,0
	for i in range(n):
		if j<leftsize and (k>=rightsize or lefthalf[j]<=righthalf[k]):
			array[i]=lefthalf[j]
			shifts+=k
			j+=1
		elif k<rightsize:
			array[i]=righthalf[k]
			k+=1
	return shifts
	
q=int(input())
for _ in range(q):
	n=int(input())
	array=[int(x) for x in input().split()]
	print(countShifts(array))