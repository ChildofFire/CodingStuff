#https://www.hackerrank.com/challenges/icecream-parlor/problem
for _ in range(int(input())):
	money=int(input())
	n=int(input())
	costlist=[int(x) for x in input().split()]
	costhash={}
	for i in range(n):
		if costlist[i] not in costhash.keys():
			costhash[costlist[i]]=[]
		costhash[costlist[i]].append(i+1)
	for i in costlist:
		if money-i in costhash.keys():
			if (money-i) == i:
				if len(costhash[i])>1:
					print(costhash[i][0],costhash[i][1])
					break
			else:
				print(costhash[i][0],costhash[money-i][0])
				break