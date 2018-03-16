#include<bits/stdc++.h>
using namespace std;
void powerset(int* a,int n)
{   int i,j,powersize;
    powersize=pow(2,n);

    for(i=0;i<powersize;i++)
        {for(j=0;j<n;j++)
          if(i & (1<<j))
             cout<<a[j]<<" ";
        cout<<"\n";
        }
}
int main()
{
    int a[1000],n,i,lrange,urange;
    cin>>n;
    for(i=0;i<n;i++)
        cin>>a[i];

    powerset(a,n);
    return 0;
}
