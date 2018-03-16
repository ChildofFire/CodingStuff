#include<iostream>
#include<string>
#include<cmath>
using namespace std;
int main()
{   long long int salpha[26], talpha[26], count=0, i, T;
    string s,t;
    cin>>T;
    while(T--)
    {
        count=0;
        cin>>s>>t;
     for(i=0;i<26;i++)
     {salpha[i]=0; talpha[i]=0;}
    for(i=0;i<s.length();i++)
        salpha[s[i]-97]++;

    for(i=0;i<t.length();i++)
        talpha[t[i]-97]++;

    for(i=0;i<26;i++)
        count+=abs(salpha[i]-talpha[i]);

    cout<<count<<endl;
    }
    return 0;
}
