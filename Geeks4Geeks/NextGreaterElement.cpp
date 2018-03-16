#include<bits/stdc++.h>
using namespace std;

void NextGreaterElement(int a[], int n)
{

        for(int i=0;i<n;i++)
        {
            int next=-1;
            for(int j=i+1;j<n;j++)
                if(a[j]>a[i]) {next=a[j]; break;}
            cout<<next<<" ";
        }
        cout<<endl;
}

int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++) cin>>a[i];
        NextGreaterElement(a,n);
    }
}
