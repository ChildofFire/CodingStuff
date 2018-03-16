import sys
string=''.join(input().strip().split()).lower()
hasher=[0]*26
for i in range(len(string)):
	hasher[ord(string[i])-97]+=1
for i in hasher:
	if i==0:
		print("not pangram")
		sys.exit()
print("pangram")