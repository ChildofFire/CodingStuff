#include<bits/stdc++.h>
using namespace std;
int prime[1000001];
int main()
{
    prime[0]=prime[1]=0;
    for(int i=2;i<1000;i++) prime[i]=1;

    for(int i=2;i<sqrt(1000);i++)
    {
        if(prime[i]==1)
            for(int j=2*i;j<1000;j+=i)
                prime[j]=0;
    }

    for(int i=2;i<1000;i++)
        if(prime[i]) cout<<i<<" ";
}
