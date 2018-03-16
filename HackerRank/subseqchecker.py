import sys
subseq="hackerrank"
q=int(input())
for i in range(q):
	string=input().strip()
	count=0
	for i in range(len(string)):
		if subseq[count]==string[i]:
			count+=1
			if count==len(subseq):
				print("YES")
				break
	if count<len(subseq):
		print("NO")
			