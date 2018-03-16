#include<bits/stdc++.h>
#define TEN 10
using namespace std;

int cost[TEN][TEN];

int minInitPoints(int cost[][TEN],int i, int j,int m, int n)
{
    if(i==m-1)
    {
        if(j==n-1)
            return (cost[i][j] > 0) ? 1: abs(cost[i][j]-1);
        return max(minInitPoints(cost,i,j+1,m,n) - cost[i][j],1);
    }

    if(j==n-1)
    {
        return max(minInitPoints(cost,i+1,j,m,n) - cost[i][j],1);
    }

    return max(min(minInitPoints(cost,i+1,j,m,n),minInitPoints(cost,i,j+1,m,n)) - cost[i][j],1);
}

int main()
{
    int t,m,n;
    cin>>t;
    while(t--)
    {
        cin>>m>>n;
        for(int i=0;i<m;i++) for(int j=0;j<n;j++) cin>>cost[i][j];
        cout<<minInitPoints(cost,0,0,m,n)<<endl;
    }
}
