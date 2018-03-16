tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

longest=len(tableData[0][0])
for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        if longest<len(tableData[j][i]):
            longest=len(tableData[j][i])

for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(longest+3),end='')
    print()

input()
        
        
