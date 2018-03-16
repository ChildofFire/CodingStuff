#include<bits/stdc++.h>
using namespace std;

int min(int a, int b)
{
    return (a>b)?b:a;
}

int minimum(int a, int b, int c)
{
    return min(min(a,b),c);
}

int minEditDistance(string s1, string s2, int m, int n)
{
    int mat[m+1][n+1];

    for(int i=0;i<=m;i++)
        for(int j=0;j<=n;j++)
            if(i==0 || j==0)
                mat[i][j]=i+j;
            else
                mat[i][j]=(s1[i-1]==s2[j-1]) ? mat[i-1][j-1] : minimum(mat[i-1][j],mat[i][j-1],mat[i-1][j-1]) + 1;

    return mat[m][n];
}

int main()
{
    int t,m,n;
    string s1,s2;
    cin>>t;
    while(t--)
    {
        cin>>m>>n;
        cin>>s1>>s2;
        cout<<minEditDistance(s1,s2,m,n)<<endl;
    }
}
