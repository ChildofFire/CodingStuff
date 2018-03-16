import re
contacts=''
for i in range(int(input())):
	x=input().split()
	if x[0]=='add':
		contacts+=' '+x[1]+' '
	else:
		pattern=x[1]+r'(\w)*'
		j=re.findall(pattern,contacts)
		print(len(j))