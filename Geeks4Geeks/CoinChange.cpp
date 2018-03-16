#include<bits/stdc++.h>
using namespace std;

int coinChange(int S[], int m, int n)
{
    int mat[n+1][m];
    for(int i=0;i<=n;i++)
        for(int j=0;j<m;j++)
            if(i==0) mat[i][j]=1;
            else
            {
                int x=(i>=S[j])? mat[i-S[j]][j] : 0;
                int y=(j>0) ? mat[i][j-1] : 0;
                mat[i][j]=x+y;
            }
    return mat[n][m-1];
}

int main()
{
    int t,n,m;
    cin>>t;
    while(t--)
    {
        cin>>m;
        int S[m];
        for(int i=0;i<m;i++) cin>>S[i];
        cin>>n;
        cout<<coinChange(S,m,n)<<endl;
    }
}
