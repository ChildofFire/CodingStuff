#include<iostream>
#include<string>
using namespace std;
int main()
{
    string s;
    long long int cl=0,cr=0,cd=0,cu=0,x,y,i;
    cin>>s;
    for(i=0;i<s.length();i++)
        if(s[i]=='L') cl++;
       else if(s[i]=='R') cr++;
       else if(s[i]=='U') cu++;
       else cd++;

       x=cr-cl; y=cu-cd;
       cout<<x<<" "<<y;

    return 0;
}
