#https://www.hackerrank.com/challenges/missing-numbers/problem

import sys

def missingNumbers(arr, brr):
    minimum=min(brr)
    lookup1=[0]*100
    lookup2=[0]*100
    for i in arr:
        lookup1[i-minimum]+=1
    for i in brr:
        lookup2[i-minimum]+=1
    result=[]
    for i in range(100):
        if lookup2[i]>lookup1[i]:
            result.append(i+minimum)
    return sorted(result)
            

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))