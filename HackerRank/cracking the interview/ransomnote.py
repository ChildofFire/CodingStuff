import sys
input()
mag={}
for word in input().strip().split():
	if word in mag.keys():
		mag[word]+=1
	else:
		mag[word]=1
note={}
for word in input().strip().split():
	if word in note.keys():
		note[word]+=1
	else:
		note[word]=1
for word in note.keys():
	if word not in mag.keys() or note[word]>mag[word]:
		print("No")
		sys.exit()

print("Yes")