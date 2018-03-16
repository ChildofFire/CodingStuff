#https://www.hackerrank.com/challenges/gridland-metro

class Interval:
	def __init__(self,start,end):
		self.start=start
		self.end=end
	def getlength(self):
		return self.end-self.start+1
	def __repr__(self):
		return "%s %s"%(self.start,self.end)

def mergeintervals(intervals):				#function to merge overlapping intervals and return total length of disjoint intervals
	intervals.sort(key=lambda x:x.start)	#sorts the intervals according to the starting column
	stack=[intervals[0]]
	for i in range(1,len(intervals)):
		top=stack[-1]
		if top.end<intervals[i].start:		#if the interval at top of stack ends before the next interval, then both are disjoint and so push the
											#new interval onto stack
			stack.append(intervals[i])
		elif top.end<intervals[i].end:		#elif the new interval starts before the end of the top interval but ends after the end of the top
											#interval, meaning both are overlapping and the new interval is not contained within the top interval.
											#so update the end col of the top interval by the end col of the new interval and push it onto stack.
			top.end=intervals[i].end
			stack.pop()
			stack.append(top)
											#else if the new interval is contained within the top interval, i.e interval[i].start>top.start and interval[i].end<top.end
											#then do nothing.
	totallength=0							
	for i in range(len(stack)):
		totallength+=stack[i].getlength()	#combined range of all disjoint intervals.
	return totallength

def lampposts(n,m,k,tracks):
	trackcellcount=0
	tracks.sort(key=lambda x:x[0])			#sort the tracks according to the row number.
	i=0
	while i<k:
		curr_row=tracks[i][0]
		intervals=[]
		while i<k and curr_row==tracks[i][0]:
			intervals.append(Interval(tracks[i][1]-1,tracks[i][2]-1))	#push all tracks in the same row into a single list of Interval type objects.
			i+=1
		trackcellcount+=mergeintervals(intervals)						#get the total length of all non-overlapping tracks in the same row.
	return n*m-trackcellcount											#no of lampposts=total cells - no of track cells.

n,m,k=[int(x) for x in input().split()]
tracks=[]
for i in range(k):
	tracks_i=[int(x) for x in input().split()]
	tracks.append(tracks_i)
print(lampposts(n,m,k,tracks))