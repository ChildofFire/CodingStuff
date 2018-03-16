class Node:							#represents a node of a graph
	def __init__(self):
		self.visited=False			#flag variable to avoid loops by revisiting nodes.
		self.neighbors=[]
		self.distance=-1			#distance from root. -1 means disconnected.

def printShortestPaths(nodelist,root):	#implements BFS by level order traversal of graph
	nodelist[root].visited=True
	nodelist[root].distance=0
	levelqueue=[root]
	while len(levelqueue)>0:
		curr=levelqueue[0]
		for i in nodelist[curr].neighbors:
			if not nodelist[i].visited:
				levelqueue.append(i)
				nodelist[i].visited=True
				nodelist[i].distance=nodelist[curr].distance+6
		levelqueue.pop(0)

	for i in nodelist:
		if i.distance!=0:
			print(i.distance,end=' ')
	print()

q=int(input())
for _ in range(q):
	n,m=[int(x) for x in input().split()]
	nodelist=[]
	for _ in range(n):
		newnode=Node()
		nodelist.append(newnode)
	for _ in range(m):
		a,b=[int(x) for x in input().split()]
		nodelist[a-1].neighbors.append(b-1)
		nodelist[b-1].neighbors.append(a-1)
	root=int(input())-1
	printShortestPaths(nodelist,root)