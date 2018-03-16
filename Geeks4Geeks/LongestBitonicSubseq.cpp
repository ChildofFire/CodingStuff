#include<bits/stdc++.h>
using namespace std;

int LBSCalc(int a[], int N)
{
    int LIS[N], LDS[N];
    LIS[0]=1;
    LDS[N-1]=1;
    for(int i=1;i<N;i++)
    {
        int max_lis=0;
        for(int j=0;j<i;j++)
            if(a[j]<a[i] && max_lis<LIS[j]) max_lis=LIS[j];
        LIS[i]=max_lis+1;
    }
    for(int i=N-2;i>=0;i--)
    {
        int max_lds=0;
        for(int j=N-1;j>i;j--)
            if(a[j]<a[i] && max_lds<LDS[j]) max_lds=LDS[j];
        LDS[i]=max_lds+1;
    }
    int max_lbs=LIS[0]+LDS[0]-1;
    for(int i=1;i<N;i++)
        if(max_lbs < LIS[i]+LDS[i]-1)
            max_lbs=LIS[i]+LDS[i]-1;
    return max_lbs;
}

int main()
{
    int T,N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        int a[N];
        for(int i=0;i<N;i++) cin>>a[i];
        cout<<LBSCalc(a,N)<<endl;
    }
}
