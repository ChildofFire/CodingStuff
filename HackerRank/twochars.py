def alternate(pair):
	for i in range(len(pair)-1):
		if pair[i]==pair[i+1]:
			return False
	return True

n=input()
string=input().strip()
sett=list(set(string))
length=0
for i in range(len(sett)):
	for j in range(i+1,len(sett)):
		pair=[temp for temp in string if temp==sett[i] or temp==sett[j]]
		if alternate(pair):
			length=max(length,len(pair))

print(length)