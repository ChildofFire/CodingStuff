#https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
#https://www.quora.com/What-is-the-logic-used-in-the-HackerRank-Maximise-Sum-problem/answer/Ajay-Gaur-5?share=196d9d7d&srid=21KB

def maxsubsum(n,m,array):
	prefix_sum=[[array[0]%m,0]]
	for i in range(1,n):
		prefix_sum.append([(prefix_sum[i-1][0]+array[i])%m,i])
	prefix_sum.sort()
	mindiff=prefix_sum[-1][0]
	for i in range(n-1):
		if prefix_sum[i][1]>prefix_sum[i+1][1]:
			if (prefix_sum[i+1][0]-prefix_sum[i][0]) < mindiff:
				mindiff=prefix_sum[i+1][0]-prefix_sum[i][0]
	return max(m-mindiff,prefix_sum[-1][0])

for _ in range(int(input())):
	n,m=[int(x) for x in input().split()]
	array=[int(x) for x in input().split()]
	print(maxsubsum(n,m,array))