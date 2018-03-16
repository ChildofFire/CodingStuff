def checkbalance(string):
	stack=[]

	for i in string:
		if i=='[' or i=='{' or i=='(':
			stack.append(i)
		else:
			if i==']':
				if len(stack)==0 or stack[len(stack)-1]!='[':
					print("NO")
					return
				else:
					stack.pop()
			elif i=='}':
				if len(stack)==0 or stack[len(stack)-1]!='{':
					print("NO")
					return
				else:
					stack.pop()
			else:
				if len(stack)==0 or stack[len(stack)-1]!='(':
					print("NO")
					return
				else:
					stack.pop()
	if len(stack)==0:
		print("YES")
	else:
		print("NO")



for i in range(int(input().strip())):
	string=input().strip()
	checkbalance(string)
