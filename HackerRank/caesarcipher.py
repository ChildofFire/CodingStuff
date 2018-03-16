r=input()
string=input().strip()
copy=""
k=int(input())
for i in range(len(string)):
	if ord(string[i]) in range(65,91):
		copy+=chr((ord(string[i])-65+k)%26+65)
	elif ord(string[i]) in range(97,123):
		copy+=chr((ord(string[i])-97+k)%26+97)
	else:
		copy+=string[i]

print(copy)