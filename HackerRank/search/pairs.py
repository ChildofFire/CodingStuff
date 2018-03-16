#https://www.hackerrank.com/challenges/pairs/problem
#!/bin/python3

import sys

def bsearch(arr,start,end,x):
	if end<=start:
		return x==arr[start]
	mid=(start+end)//2
	if x==arr[mid]:
		return True
	if x>arr[mid]:
		return bsearch(arr,mid+1,end,x)
	if x<arr[mid]:
		return bsearch(arr,start,mid-1,x)

def pairs(n,k,arr):
    arr.sort()
    count=0
    for i in range(n-1):
    	if bsearch(arr,i+1,n-1,arr[i]+k):
    		count+=1
    return count
            

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(n,k, arr)
    print(result)
