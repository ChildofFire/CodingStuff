def coinchange(coins,m,n):
	mat=[]				#mat[i][j] represents the number of ways to make a change of amount 'i' using 'j+1' elements of the 'coins' array.	
	
	for _ in range(n+1):	#initialization
		mat.append([None]*(m))
	
	for i in range(n+1):
		for j in range(m):
			if i==0:
				mat[i][j]=1	#first row is all 1s as there is 0 amount. just one way to do that.
			else:
				x=mat[i-coins[j]][j] if i>=coins[j] else 0	#no. of ways to make change for 'i-coins[j]' dollars with 'j+1' type of coins.
				y=mat[i][j-1] if j>0 else 0					#no. of ways to make change for 'i' dollars with 'j' type of coins.
				mat[i][j]=x+y

	return mat[n][m-1]		#last entry of the matrix represents the final answer, i.e, number of ways to make change for n dollars using m type of coins.


n,m=[int(x) for x in input().split()]
coins=[int(x) for x in input().split()]
coins.sort()
print(coinchange(coins,m,n))