#include<bits/stdc++.h>
#define mod 1000000007
using namespace std;

long long power(long long int a,long long int b)
{
    long long residue=1;
    while(b>0)
    {
        if(b&1) residue=(residue*a) % mod;
        a=(a*a)%mod;
        b/=2;
    }
    return residue;
}

int main()
{   long long sum=0,p,p2,p11,i;
    string s;
    cin>>s;
    for(i=0;i<s.length();i++)
    {
        p2=power(2LL,(long long)i);
        p11=power(11LL,(long long)s.length()-i-1);
        p=(p2*p11)%mod;
        p=(p*(s[i]-48))%mod;
        sum=(sum+p)%mod;
    }
    cout<<sum<<endl;
    return 0;
}
