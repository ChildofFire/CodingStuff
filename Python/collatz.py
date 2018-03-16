def collatz(number):
    print(number)
    if number==1:
        return
    if number%2:
        collatz(3*number+1)
    else:
        collatz(number//2)


collatz(int(input("enter value")))

input()
