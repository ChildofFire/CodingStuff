#https://www.hackerrank.com/challenges/cavity-map/problem

def printMap(squaremap):
	if len(squaremap)>=3:
		i=1
		for i in range(1,len(squaremap)-1):
			for j in range(1,len(squaremap)-1):
				if areNeighborsDigits(squaremap,i,j) and isCavity(squaremap,i,j):
					squaremap[i][j]='X'
	for i in range(len(squaremap)):
		print(''.join(squaremap[i]))

squaremap=[]
for _ in range(int(input())):
	squaremap.append(list(input()))
printMap(squaremap)