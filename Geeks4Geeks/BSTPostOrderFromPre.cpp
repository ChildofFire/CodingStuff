#include<bits/stdc++.h>
using namespace std;

int findBigger(int a[], int n)
{
    int i;
    for(i=1;i<n;i++)
    {
        if(a[i]>a[0]) break;
    }
    return i;
}

bool PrintPostOrder(int pre[], int n)
{
    if(n==1) {cout<<pre[0]<<" "; return true;}

    int index=findBigger(pre,n);
    int counter=0;
    for(int i=index+1;i<n;i++)
    {
        if(pre[i] < pre[0]) {counter++; break;}
    }
    if(counter) {return false;}

    bool res=true;
    if(index>1) res=PrintPostOrder(pre+1,index-1);
    if(index<n) res=res && PrintPostOrder(pre+index,n-index);
    if(res)
    cout<<pre[0]<<" ";
    return res;
}

int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        int pre[n];
        for(int i=0;i<n;i++) cin>>pre[i];
        if(!PrintPostOrder(pre,n)) cout<<"NO";
        cout<<endl;
    }
}
