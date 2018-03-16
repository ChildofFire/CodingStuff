#https://www.hackerrank.com/challenges/lilys-homework/problem
def countSwaps(array,n,arraysorted,hashmap):
	visited=[False]*n
	total_swaps=0
	for i in range(n):
		if not visited[i] and array[i]!=arraysorted[i]:
			j=i
			cycle_len=0
			while not visited[j]:
				visited[j]=True
				cycle_len+=1
				j=hashmap[arraysorted[j]]
			total_swaps+=cycle_len-1
	return total_swaps
def minSwaps(array,n):
	hashmap={}
	for i in range(n):
		hashmap[array[i]]=i
	arraysorted=sorted(array)
	arrayrevsorted=sorted(array,reverse=True)
	fwdswaps=countSwaps(array,n,arraysorted,hashmap)
	bckswaps=countSwaps(array,n,arrayrevsorted,hashmap)
	return min(fwdswaps,bckswaps)



n=int(input())
array=[int(x) for x in input().split()]
print(minSwaps(array,n))