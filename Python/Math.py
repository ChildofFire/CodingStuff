#Python script to find the number of digits in an integer
import math

def returnDigits(x):
    return math.ceil(math.log10(float(x)))

x=int(input())


if int(x)==0 or int(x)==1:
    print(1)
elif int(x)>1:
    print(returnDigits(x))
else:
    print("Wrong input")

input()
