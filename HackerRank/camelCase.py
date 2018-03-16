def camelcase(string):
	count=1
	for i in range(0,len(string)):
		if string[i].isupper():
			count+=1
	print (count)



string=input()
camelcase(string)