for _ in range(int(input())):
	n=int(input())
	if n==1:
		print("Not prime")
	elif n==2 or n==3:
		print("Prime")
	else:
		mod=n%6

		if mod==1 or mod==5:
			flag=1
			for i in range(2,int(n**0.5)+1):
				if not n%i:
					flag-=1
					break
			if not flag:
				print("Not prime")
			else:
				print ("Prime")
		else:
			print("Not prime")