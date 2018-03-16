
#include<iostream>
#include<string>
using namespace std;
int main()
{   long long int a[100000],sum=0,i,l;
    string s;
    cin>>s;
    l=s.length();
    for(i=0;i<s.length();i++)
       {
         a[i]=s[i]-96;
         sum+=a[i];
         }

         if(((a[l-1]==0)||(a[l-1]==2)||(a[l-1]==4)||(a[l-1]==6)||(a[l-1]==8)) && (sum%3==0))
            cout<<"YES";
         else
            cout<<"NO";
    return 0;
}
