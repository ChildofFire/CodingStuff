import time
start=time.time()
primeswith3=[x for x in range(2,101) if x%10 == 3 and all(x%d !=0 for d in range(2,int(x**(0.5))+1))]
print(len(primeswith3))
end=time.time()
print(end-start)

input()

