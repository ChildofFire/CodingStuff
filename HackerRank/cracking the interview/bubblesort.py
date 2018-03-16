def bubblesort(a):
	count=0
	for i in range(len(array)-1):
		for j in range(i+1,len(array)):
				if a[i]>a[j]:
					count+=1
					a[i],a[j]=a[j],a[i]
	return count,a[0],a[len(a)-1]


n=int(input())
array=[int(x) for x in input().split()]
count,f,l=bubblesort(array)
print("Array is sorted in %s swaps.\nFirst Element: %s\nLast Element: %s"%(count,f,l))