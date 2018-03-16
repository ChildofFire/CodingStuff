#https://www.hackerrank.com/challenges/torque-and-development/problem

class Node:
	def __init__(self):
		self.neighbors=[]

def connectedComponents(Graph,n):
	visited=[False]*n
	connectedregions=0
	connectedlist=[]
	for i in range(n):
		if not visited[i]:
			visited[i]=True
			connectedregions+=1
			nodecount=0
			queue=[Graph[i]]
			while len(queue)>0:			#BFS to traverse the graph (though DFS would also be equally fine!).
				curr=queue[0]
				for i in curr.neighbors:
					if not visited[i]:
						visited[i]=True
						queue.append(Graph[i])
				queue.pop(0)
				nodecount+=1
			connectedlist.append(nodecount)
	return connectedregions,connectedlist



def minCost(n,libcost,roadcost,Graph):
	if roadcost>libcost:
		return n*libcost
	connectedregions,connectedlist=connectedComponents(Graph,n)	#connectedregions=number of connected subgraphs
																#connectedlist=number of nodes in each connected subgraph
	totallibcost=connectedregions*libcost
	totalroadcost=0
	for i in connectedlist:
		totalroadcost+=(i-1)*roadcost
	return totallibcost+totalroadcost


for _ in range(int(input())):
	n,m,libcost,roadcost=[int(x) for x in input().split()]
	Graph=[Node() for x in range(n)]
	for _ in range(m):
		x,y=[int(i)-1 for i in input().split()]
		Graph[x].neighbors.append(y)
		Graph[y].neighbors.append(x)
	print(minCost(n,libcost,roadcost,Graph))