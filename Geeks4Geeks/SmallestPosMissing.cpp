#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        int a[N],i,temp[10000]={0};
        for(i=0;i<N;i++) { cin>>a[i]; if(a[i]>0) temp[a[i]]++;}

        for(i=1;i<=N;i++)
            if(temp[i]==0) break;
        cout<<i<<endl;
    }
}
