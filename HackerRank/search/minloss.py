#!/bin/python3

import sys

def minimumLoss(price,n):
    sortedprice=sorted(price)
    lookup={}
    for i in range(n):
        lookup[price[i]]=i
    mindiff=0
    for i in range(n-1):
        if lookup[sortedprice[i]]>lookup[sortedprice[i+1]]:
            if mindiff==0 or mindiff>(sortedprice[i+1]-sortedprice[i]):
                mindiff=sortedprice[i+1]-sortedprice[i]
    return mindiff

if __name__ == "__main__":
    n = int(input().strip())
    price = list(map(int, input().strip().split(' ')))
    result = minimumLoss(price,n)
    print(result)