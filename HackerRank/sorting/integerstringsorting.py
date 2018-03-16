#https://www.hackerrank.com/challenges/big-sorting/problem
def sorter(a,b):
	if len(a)==len(b):
		return a<b
	return len(a)<len(b)

n=['2','12','11111','22222']
n.sort(key=int)
print(n)