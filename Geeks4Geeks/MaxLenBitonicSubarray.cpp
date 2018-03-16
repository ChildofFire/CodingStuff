#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        int a[N];
        for(int i=0;i<N;i++) cin>>a[i];
         int increasing[N], decreasing[N];
        increasing[0]=1; decreasing[N-1]=1;
        for(int i=1;i<N;i++)
        {
            if(a[i]>=a[i-1]) increasing[i]=increasing[i-1]+1;
            else increasing[i]=1;
        }
        for(int i=N-2;i>=0;i--)
        {
            if(a[i]>=a[i+1]) decreasing[i]=decreasing[i+1]+1;
            else decreasing[i]=1;
        }
        int max_len=increasing[0]+decreasing[0]-1, k=0;
        for(int i=1;i<N;i++)
            if(increasing[i]+decreasing[i]-1 > max_len)
                { max_len=increasing[i]+decreasing[i]-1; k=i;}
        cout<<max_len<<" "<<k<<endl;
    }
}
