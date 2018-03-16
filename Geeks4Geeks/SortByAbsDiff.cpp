#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N,X;
    cin>>T;
    while(T--)
    {
        cin>>N>>X;
        int a[N];
        for(int i=0;i<N;i++) cin>>a[i];
        multimap<int,int> m;
        for(int i=0;i<N;i++)
            m.insert(make_pair(abs(X-a[i]),a[i]));
        int i=0;
        for(map<int,int>::iterator iter=m.begin();iter!=m.end();iter++)
            a[i++]=(*iter).second;
        for(int j=0;j<N;j++) cout<<a[j]<<" "; cout<<endl;
    }
}
