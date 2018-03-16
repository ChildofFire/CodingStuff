#include<bits/stdc++.h>
using namespace std;

void powerset(string s,int n,int m)
{   int i,j,powersize;
    powersize=pow(2,n-m+1);

    for(i=0;i<powersize;i++)
        {for(j=n;j<=m;j++)
          if(i & (1<<(j-n)))
             cout<<s[j]<<" ";
        cout<<"\n";
        }
}

int main()
{
    string s;
    int lrange,urange;
    cin>>s;
    cin>>lrange>>urange;
    powerset(s,lrange,urange);


    return 0;
}
