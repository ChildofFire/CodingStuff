def median(X):
	if len(X)%2:
		med=X[len(X)//2]
	else:
		mid=len(X)//2
		med=(X[mid-1]+X[mid])//2
	return med

input()
X=[int(x) for x in input().split()]
X.sort()
q1=median(X[:len(X)//2])
q2=median(X)
if len(X)%2:
	q3=median(X[len(X)//2+1:])
else:
	q3=median(X[len(X)//2:])
print("%s\n%s\n%s"%(q1,q2,q3))