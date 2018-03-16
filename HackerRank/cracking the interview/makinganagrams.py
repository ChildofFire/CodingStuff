string1=input().strip()
string2=input().strip()
hasher1=[0]*26
hasher2=[0]*26
for i in string1:
	hasher1[ord(i)-97]+=1
for i in string2:
	hasher2[ord(i)-97]+=1
count=0
for i in range(26):
	count+=abs(hasher1[i]-hasher2[i])
print(count)