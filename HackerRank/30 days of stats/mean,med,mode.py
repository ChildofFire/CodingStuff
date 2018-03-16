def meanmedmode(X):
	total=0
	minimum=X[0]
	for x in X:
		total+=x
		if minimum>x:
			minimum=x
	mean=total/len(X)
	if len(X)%2:
		median=X[len(X)//2]
	else:
		mid=len(X)//2
		median=(X[mid]+X[mid-1])/2
	freq={}
	for x in range(len(X)):
		freq[X[x]]=freq.get(X[x],0)+1
	mode=minimum
	freqmax=freq[minimum]
	for x in range(1,len(X)):
		if freqmax<freq[X[x]]:
			mode=X[x]
			freqmax=freq[X[x]]

	print("%.1f\n%.1f\n%s"%(mean,median,mode))

input()
X=[int(x) for x in input().split()]
meanmedmode(sorted(X))