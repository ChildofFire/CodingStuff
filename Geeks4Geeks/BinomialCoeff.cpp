#include<bits/stdc++.h>
#define M 1000000007

using namespace std;

long long int mat[1001][801];

void initialize()
{
    for(int i=0;i<1001;i++)
        for(int j=0;j<801;j++)
            mat[i][j]=0;
}

long long int binomial(int n ,int r)
{
    if(mat[n][r]==0)
    {
        if(r==0 || r==n) mat[n][r]=1;
        else
            if(n<r) return 0;
            else
            mat[n][r]=(binomial(n-1,r-1)%M+binomial(n-1,r)%M)%M;
    }

    return mat[n][r];

}

int main()
{
    int t,n,r;
    initialize();
    cin>>t;
    while(t--)
    {
        cin>>n>>r;
        cout<<binomial(n,r)<<endl;
    }
}
