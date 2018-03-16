#https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

def towerCount(pos,n,k):
	towercount=0
	i=0
	while i<n:
		covereddist=pos[i]+k
		while i<n and pos[i]<=covereddist:
			i+=1
		i-=1
		towercount+=1
		covereddist=pos[i]+k
		while i<n and pos[i]<=covereddist:
			i+=1
	return towercount


n,k=[int(x) for x in input().split()]
pos=[int(x) for x in input().split()]
print(towerCount(sorted(pos),n,k))