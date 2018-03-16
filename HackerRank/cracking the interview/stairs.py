ways=[1,1,2]+[0]*34

def stairs(n):
	if not ways[n]:
		ways[n]=(stairs(n-1)+stairs(n-2)+stairs(n-3))
	return ways[n]

for _ in range(int(input())):
	n=int(input())
	print(stairs(n))