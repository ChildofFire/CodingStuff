#include<bits/stdc++.h>
using namespace std;

int maximum(string s, int n)
{
    int temp[n];
    for(int i=0;i<n;i++) temp[i]=0;
    for(int i=0;i<n-1;i++)
       {
            if(s[i]=='1')
              {for(int j=i+1;j<n;j++)
                if(s[j]=='1')
                    temp[i]++;
              }
       }
    int numberofstrings=0;
    for(int i=0;i<n;i++)
        numberofstrings+=temp[i];
    return numberofstrings;
}

int main()
{
    int t,n;
    string s;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cin>>s;
        cout<<maximum(s,n)<<endl;
    }
}
