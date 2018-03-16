#finds median of a running list of integers.
#running list means that elements are inserted one by one
#and median is printing after each insertion.

def findindex(a,x,start,end):
	if end<=start:
		return start+1 if x>a[start] else start
	mid=int((start+end)/2)
	if x==a[mid]:
		return mid+1
	if x>a[mid]:
		return findindex(a,x,mid+1,end)
	return findindex(a,x,start,mid-1)

n=int(input())
a=[]
for i in range(n):
	x=int(input())
	if i==0:
		index=0
	elif i==1:
		index=0 if x<a[0] else 1
	else:
		index=findindex(a,x,0,len(a)-1)
		
	a.insert(index,x)
	if len(a)%2==0:
		median=float((a[int(len(a)/2)-1]+a[int(len(a)/2)])/2)
	else:
		median=float(a[int(len(a)/2)])
	print("%.1f"%median)