class Cell:
	def __init__(self,data):
		self.data=data
		self.visited=False
	def __repr__(self):
		return ("%s %s"%(self.data,self.visited))

def findFilledCells(grid,i,j,n,m):
	if i not in range(0,n) or j not in range(0,m) or grid[i][j].visited or grid[i][j].data==0:
		return 0
	grid[i][j].visited=True
	return 1+findFilledCells(grid,i-1,j-1,n,m)+findFilledCells(grid,i-1,j,n,m)\
	+findFilledCells(grid,i-1,j+1,n,m)+findFilledCells(grid,i,j-1,n,m)\
	+findFilledCells(grid,i,j+1,n,m)+findFilledCells(grid,i+1,j-1,n,m)\
	+findFilledCells(grid,i+1,j,n,m)+findFilledCells(grid,i+1,j+1,n,m)


def findMaxRegion(grid,n,m):
	maxFilledCells=0
	for i in range(n):
		for j in range(m):
			if not (grid[i][j].visited) and grid[i][j].data==1:
				noOfFilledCells=findFilledCells(grid,i,j,n,m)
				if maxFilledCells<noOfFilledCells:
					maxFilledCells=noOfFilledCells
	return maxFilledCells

n=int(input())
m=int(input())
grid=[]
for _ in range(n):
	cells=[Cell(int(x)) for x in input().split()]
	grid.append(cells)
print(findMaxRegion(grid,n,m))