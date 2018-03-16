#https://www.hackerrank.com/challenges/runningtime/problem

import sys

def runningTime(arr):
    counter=0
    for i in range(1,len(arr)):
        curr=arr[i]
        j=i-1
        while j>=0 and arr[j]>curr:
            arr[j+1]=arr[j]
            j-=1
            counter+=1
        arr[j+1]=curr
        
    return counter
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
