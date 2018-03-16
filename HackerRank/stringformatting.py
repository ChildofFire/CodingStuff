def format(number):
	length=len(bin(number))
	for i in range(1, number+1):
		print (str(i).rjust(length), str(oct(i)[2:]).upper().rjust(length), str(hex(i)[2:]).upper().rjust(length), str(bin(i)[2:]).rjust(length))

number=int(input())
format(number)