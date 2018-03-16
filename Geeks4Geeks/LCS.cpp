#include<bits/stdc++.h>
using namespace std;

int maximum(int a, int b)
{
    return (a>b)? a: b;
}

string LCS(string s1, string s2, int a, int b)
{
    int mat[a+1][b+1];
    for(int i=0;i<=a;i++)
        for(int j=0;j<=b;j++)
            if(i==0 || j==0)
                mat[i][j]=0;
            else
                mat[i][j]=(s1[i-1]==s2[j-1])? mat[i-1][j-1]+1 : maximum(mat[i-1][j],mat[i][j-1]);

    int i=a, j=b;
    string str;
    while(mat[i][j]!=0)
    {
        if(mat[i][j]!=maximum(mat[i-1][j],mat[i][j-1])) {str+=s1[i-1]; i--; j--;}
        else
            {
                if(mat[i][j]==mat[i-1][j]) i--;
                else j--;
            }
    }

    reverse(str.begin(),str.end());
    return str;

}

int main()
{
    int t,a,b; string s1, s2;
    cin>>t;
    while(t--)
    {
        cin>>a>>b;
        cin>>s1>>s2;
        cout<<LCS(s1,s2,a,b)<<endl;
    }
}
