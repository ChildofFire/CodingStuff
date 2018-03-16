#https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/programming-competition
n=int(input())
leaderboard=[]
for _ in range(n):
	name,dec,jan=input().split()
	dec,jan=int(dec),int(jan)
	leaderboard.append([name,dec,jan,jan-dec])
maxscore=0
for i in leaderboard:
	if maxscore<i[3]:
		maxscore=i[3]
winner=""
for i in leaderboard:
	if i[3]==maxscore:
		#winners.append([i[0],i[1]])
		winner=i[0]
		break
#winners.sort(key=lambda x:x[1])
print(winner,maxscore)