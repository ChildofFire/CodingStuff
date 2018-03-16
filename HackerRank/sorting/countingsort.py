#https://www.hackerrank.com/challenges/countingsort4/problem
n=int(input())
hasher={}

for i in range(n):
	number,string=input().split()
	number=int(number)
	if i<n//2:
		string="-"
	hasher[number]=hasher.get(number,"")+" "+string

finalstring=""
for i in range(100):
	if i in hasher.keys():
		finalstring+=hasher[i]
print(finalstring.strip())