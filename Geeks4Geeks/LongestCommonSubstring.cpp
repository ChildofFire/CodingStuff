#include<bits/stdc++.h>
using namespace std;

int LongestCommonSubstring(string X, string Y)
{
    int LCSuffix[X.length()+1][Y.length()+1], length=0;
    for(int i=0;i<=X.length();i++)
    {
        for(int j=0;j<=Y.length();j++)
        {
            if(i==0 || j==0) LCSuffix[i][j]=0;
            else if(X[i-1]==Y[j-1])
                {
                    LCSuffix[i][j]=LCSuffix[i-1][j-1]+1;
                    if(LCSuffix[i][j]>length) length=LCSuffix[i][j];
                }
            else LCSuffix[i][j]=0;
        }
    }
    return length;
}

int main()
{
    int T,M,N;
    string S1,S2;
    cin>>T;
    while(T--)
    {
        cin>>M>>N;
        cin>>S1>>S2;
        cout<<LongestCommonSubstring(S1,S2)<<endl;
    }
}
