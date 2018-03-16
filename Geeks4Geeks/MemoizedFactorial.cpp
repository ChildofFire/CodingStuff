#include<bits/stdc++.h>
using namespace std;

long long int lookup[21]={0};

void initializer()
{
    for(int i=0;i<20;i++) lookup[i]=0;
}

long long int fac(int n)
{
    if(lookup[n]==0)
    {
        if(n<=1) lookup[n]=1;
        else lookup[n]=n*fac(n-1);
    }
    return lookup[n];
}

int main()
{

    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        initializer();
        cout<<fac(n)<<endl;
    }
}
