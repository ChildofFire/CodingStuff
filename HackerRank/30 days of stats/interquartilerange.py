def median(X):
	if len(X)%2:
		med=float(X[len(X)//2])
	else:
		mid=len(X)//2
		med=float((X[mid-1]+X[mid])//2)
	return med

def constructS(X,F):
	S=[]
	for i in range(len(F)):
		while F[i]:
			S.append(X[i])
			F[i]-=1
	return S


input()
X=[int(x) for x in input().split()]
F=[int(f) for f in input().split()]
S=constructS(X,F)
S.sort()
q1=median(S[:len(S)//2])
q2=median(S)
if len(S)%2:
	q3=median(S[len(S)//2+1:])
else:
	q3=median(S[len(S)//2:])
print("%.1f"%(q3-q1))