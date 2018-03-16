def getmean(X):
	total=0
	for i in X:
		total+=i
	return total/len(X)

def sd(X,mean):
	variance=0
	for i in X:
		variance+=(i-mean)**2
	return (variance/len(X))**0.5

input()
X=[int(x) for x in input().split()]
print("%.1f"%sd(X,getmean(X)))