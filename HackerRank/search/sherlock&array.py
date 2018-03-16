#https://www.hackerrank.com/challenges/sherlock-and-array/problem

import sys

def solve(a,n):
    if n==1:
        return "YES"
    if n==2:
        return "NO"
    leftsum=a[0]
    rightsum=0
    for x in a[2:]:
        rightsum+=x
    for i in range(1,n-1):
        if leftsum==rightsum:
            return "YES"
        leftsum+=a[i]
        rightsum-=a[i+1]
    return "NO"

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a,n)
    print(result)