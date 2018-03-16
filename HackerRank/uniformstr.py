string=input().strip()
n=int(input())

hasher={}
uniform=set()
for i in range(26):
	hasher[chr(i+97)]=i+1

count=1
for i in range(len(string)):
	weight=hasher[string[i]]
	count=count+1 if (i+1 != len(string) and string[i]==string[i+1]) else 1
	uniform.add(weight*count)

for i in range(n):
	print ("Yes" if int(input()) in uniform else "No")
