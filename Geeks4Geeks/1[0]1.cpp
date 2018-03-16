#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T; string S;
    cin>>T;
    while(T--)
    {
        cin>>S;
        int counter=0,i,j;
        for(i=0;i<S.length();i++)
            if(S[i]=='1')
                {
                    for(j=i+1;j<S.length();j++)
                    {
                        if(j==i+1) {if(S[j]!='0') break;}
                        else
                        {if(S[j]=='1') {counter++; i=j-1; break;}
                        else if(S[j]!='0') break;
                        }
                    }
                }
        cout<<counter<<endl;
    }
}
