#include<iostream>
#include<string>
using namespace std;
int main()
{   long long int N,i,count=0,j;
    string s;
    char s2[5]={'a','e','i','o','u'};
    cin>>N;
    cin>>s;

    for(j=0;j<5;j++)
    for(i=0;i<s.length();i++)
    {
        if(s[i]==s2[j])
        { count++; break;}
    }

       if(count==5)
        cout<<"YES";
       else
          cout<<"NO";




    return 0;
}
