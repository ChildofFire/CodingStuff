#include<iostream>
using namespace std;
int main()
{
    long long int N,A[100000],counter[100000]={0},supercount=0,i,big;
    cin>>N;
    for(i=0;i<N;i++)
    {cin>>A[i];
    if(i==0) big=A[i];
    else if(big<A[i]) big=A[i];
    counter[A[i]]++;
    }

    for(i=0;i<=big;i++)
    {
        if(counter[i]>1)
            supercount+=counter[i]*(counter[i]-1)/2;
    }

    cout<<supercount<<endl;
    return 0;
}
