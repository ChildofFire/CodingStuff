mat=[(1,2,3),(4,5,6),(7,8,9)]

for i in mat:
    print (i)

tmat=zip(*mat)

print("\n")
for i in tmat:
    print (i)
    
input()
