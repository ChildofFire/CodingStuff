def reduce(string):
	stack=[]
	for i in range(0,len(string)):
		if len(stack)==0:
			stack.append(string[i])
		else :
			if stack[len(stack)-1]==string[i]:
				stack.pop()
			else :
				stack.append(string[i])
	if len(stack)==0:
		print("Empty String")
	else:
		print(''.join(stack))


string=input()
reduce(string)