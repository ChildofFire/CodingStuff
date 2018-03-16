string=input().strip()
mask="SOS"*(int(len(string)/3))
count=0
for i in range(0,len(string)):
	if ord(string[i])-ord(mask[i]):
		count+=1

print(count)
