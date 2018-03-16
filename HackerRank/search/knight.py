#https://www.hackerrank.com/challenges/knightl-on-chessboard/problem

def shortestPath(n,a,b):
	cellqueue=[[0,0]]
	visited[0][0]=True
	possiblepaths=[[a,b],[a,-1*b],[-1*a,b],[-1*a,-1*b],[b,a],[-1*b,a],[b,-1*a],[-1*b,-1*a]]
	distancequeue=[0]
	while len(cellqueue)>0:
		if cellqueue[0][0]==n-1 and cellqueue[0][1]==n-1:
			return distancequeue[0]
		for i in range(8):

			neighbor=[cellqueue[0][0]+possiblepaths[i][0],cellqueue[0][1]+possiblepaths[i][1]]
			if neighbor[0] in range(n) and neighbor[1] in range(n) and not visited[neighbor[0]][neighbor[1]]:
				cellqueue.append(neighbor)
				distancequeue.append(distancequeue[0]+1)
				visited[neighbor[0]][neighbor[1]]=True
		cellqueue.pop(0)
		distancequeue.pop(0)
	return -1

n=int(input())
answer=[]
for i in range(n):
	answer.append([-1 for j in range(n)])

for a in range(1,n):
	for b in range(1,a+1):
		if a==b:
			if (n-1)%a==0:
				answer[a][b]=(n-1)//a
			
		else:
			for i in range(n):
				visited=[]
				for i in range(n):
					visited.append([False for j in range(n)])
			answer[a][b]=shortestPath(n,a,b)
		
for a in range(1,n):
	for b in range(a+1,n):
		answer[a][b]=answer[b][a]

for i in range(1,n):
	for j in range(1,n):
		print(answer[i][j],end=' ')
	print()