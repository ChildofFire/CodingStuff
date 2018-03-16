#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        int a[N+1],i;
        for(i=0;i<N;i++) cin>>a[i];

        a[N]=a[N-1]-1;

        for(i=0;i<N;i++) if(a[i]>a[i+1]) break;

        cout<<(i+1)%N<<endl;
    }
}
