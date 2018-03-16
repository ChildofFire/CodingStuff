#include<bits/stdc++.h>
#define mod 1000000007
using namespace std;

long long int power(int a, int b)
{
    long long int residue=1;
    while(b>0)
    {
        if(b&1) residue=(residue*a) % mod;
        a=(a*a)%mod;
        b/=2;
    }
    return residue;
}

int main()
{   long long int sum=0,p,p2,p11;
    string s;
    cin>>s;
    for(i=0;i<s.length();i++)
    {
        p2=power(2,i);
        p11=power(11,s.length()-i-1);
        p=(p2*p11)%mod;
        p=(p*(s[i]-48))%mod;
        sum=(sum+p)%mod;
    }
    cout<<sum<<endl;
    return 0;
}
