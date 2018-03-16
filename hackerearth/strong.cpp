#include<bits/stdc++.h>
using namespace std;

long long fact(long long a)
{
    if(a==0) return 1;
    else if(a==1) return 1;
    else return (a*fact(a-1));
}
int main()
{

    long long T,i,A[10],N,number,sum;
    for(i=0;i<10;i++)
    {
        A[i]=fact(i);
    }

    cin>>T;
    while(T--)
    {
        cin>>N;
        number=N;
        sum=0;
        while(N!=0)
        {
            sum+=A[N%10];
            N/=10;
        }

        if(sum==number) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;

    }
return 0;
}
