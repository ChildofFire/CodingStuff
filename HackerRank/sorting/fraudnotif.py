#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

def countingsortMedian(counter,d):
	medianpos=d//2+1 if d%2 else d//2
	i,count=0,0
	while count<medianpos:
		count+=counter[i]
		i+=1
	if count>medianpos or d%2:
		return i-1
	j=i		#control reaches here only when 'count' is equal to 'medianpos' AND number of elements 'd' is even.
	while counter[j]==0:
		j+=1
	return (i-1+j)/2

def notifCount(exp,n,d):
	counter=[0]*201
	for i in range(d):
		counter[exp[i]]+=1
	median=countingsortMedian(counter,d)
	notifCounter=1 if exp[d]>=2*median else 0
	for i in range(1,n-d):
		counter[exp[i-1]]-=1
		counter[exp[i+d-1]]+=1
		median=countingsortMedian(counter,d)
		if exp[i+d]>=2*median:
			notifCounter+=1
	return notifCounter


n,d=[int(x) for x in input().split()]
exp=[int(i) for i in input().split()]
print(notifCount(exp,n,d))