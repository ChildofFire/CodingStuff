#include<bits/stdc++.h>
#define T 20

using namespace std;
int cost[20][20];

void initialize()
{for(int i=0;i<20;i++) for(int j=0;j<20;j++) cost[i][j]=0;}

int max(int a, int b)
{
    return (a>b)? a:b;
}

int maxCost(int cost[][20],int n)
{
    int dp[n][n];
    for(int j=0;j<n;j++) dp[n-1][j]=cost[n-1][j];

    for(int i=n-2;i>=0;i--)
        for(int j=n-1;j>=0;j--)
                if(j==0)
                    dp[i][j]=cost[i][j]+max(dp[i+1][j],dp[i+1][j+1]);
                else if(j==n-1)
                    dp[i][j]=cost[i][j]+max(dp[i+1][j],dp[i+1][j-1]);
                else
                    dp[i][j]=cost[i][j]+max(max(dp[i+1][j],dp[i+1][j-1]),dp[i+1][j+1]);

    int maxcost=dp[0][0];

    for(int j=0;j<n;j++)
        if(dp[0][j]>maxcost)
            maxcost=dp[0][j];

    return maxcost;
}

int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        initialize();
        for(int i=0;i<n;i++) for(int j=0;j<n;j++) cin>>cost[i][j];
        cout<<maxCost(cost,n)<<endl;
    }
}
