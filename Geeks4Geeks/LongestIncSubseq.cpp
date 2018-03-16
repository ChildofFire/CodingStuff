#include<bits/stdc++.h>
using namespace std;

int LISCalc(int a[], int N)
{
    int LIS[N];
    LIS[0]=1;
    for(int i=1;i<N;i++)
    {
        int max_lis=0;
        for(int j=0;j<i;j++)
            if(a[j]<a[i] && LIS[j]>max_lis)
                max_lis=LIS[j];
        LIS[i]=max_lis+1;
    }
    int max_lis=LIS[0];
    for(int i=0;i<N;i++)
        if(max_lis<LIS[i]) max_lis=LIS[i];
    return max_lis;
}

int main()
{
    int T,N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        if(N==0) cout<<0<<endl;
        else
        {int a[N];
        for(int i=0;i<N;i++) cin>>a[i];
        cout<<LISCalc(a,N)<<endl;
        }
    }
}
