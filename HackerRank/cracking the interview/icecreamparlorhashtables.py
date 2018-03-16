for _ in range(int(input())):
	money=int(input())
	n=int(input())
	costlist=[int(x) for x in input().split()]
	costhash={}
	for i in range(n):
		costhash[costlist[i]]=costhash.get(costlist[i],"")+" "+str(i+1)
	for i in costlist:
		if money-i in costhash:
			indices1=costhash[i].split()
			indices2=costhash[money-i].split()
			if (money-i)==i:
				print(indices1[0],indices1[1])
				break
			else:
				print(indices1[0],indices2[0])
				break