#https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/winning-lottery-ticket
pairs={}
for i in range(1,1024):
        pairs[i]=[j for j in range(1,1024) if i|j==1023]
#pairs[1023]=[j for j in range(1023)]

counter=[0]*1024
for _ in range(int(input())):
        string=''.join(set(input().strip()))
        binary=0
        for c in string:
                binary+=2**int(c)
        counter[binary]+=1
total_pairs=0
for i in pairs.keys():
        pairsum=0
        for j in pairs[i]:
                pairsum+=counter[j]-1 if i==1023 and j==1023 else counter[j]
        total_pairs+=counter[i]*pairsum
        
print(total_pairs//2)
