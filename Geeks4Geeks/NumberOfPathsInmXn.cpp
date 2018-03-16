#include<bits/stdc++.h>
using namespace std;

long int numberOfPaths(int m,int n)
{
    unsigned int M=1000000007;
    if(m==1 || n==1) return 1;

    return numberOfPaths(m-1,n)%M+numberOfPaths(m,n-1)%M;
}

int main()
{
    int t,m,n;
    cin>>t;
    while(t--)
    {
        cin>>m>>n;
        cout<<numberOfPaths(m,n)<<endl;
    }
}
