n,d=[ int(c) for c in input().strip().split()]
array=[int(c) for c in input().strip().split()]*2
#print(array[d%n:d%n+n])
string=' '.join([str(c) for c in array[d%n:d%n+n]])
print(string)