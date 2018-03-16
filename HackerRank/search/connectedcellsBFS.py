#https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

def maxRegion(grid,n,m):
	maxregionsize=0
	for i in range(n):
		for j in range(m):
			if grid[i][j]==1:
				grid[i][j]=0
				regionsize=0
				paths=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
				queue=[[i,j]]
				while len(queue)>0:
					curr=queue[0]
					for a,b in paths:
						j,k=curr[0]+a,curr[1]+b
						if j in range(n) and k in range(m) and grid[j][k]==1:
							grid[j][k]=0
							queue.append([j,k])
					queue.pop(0)
					regionsize+=1
				if regionsize>maxregionsize:
					maxregionsize=regionsize
	return maxregionsize

n=int(input())
m=int(input())
grid=[]
for i in range(n):
	grid.append([int(x) for x in input().split()])
print(maxRegion(grid,n,m))