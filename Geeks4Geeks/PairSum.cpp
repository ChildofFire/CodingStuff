#include<bits/stdc++.h>
using namespace std;

string pairSum(int arr[], int N, int X)
{
    int l=0, r=N-1;

    while(l<r)
    {
        if((arr[l]+arr[r])==X) return "Yes";
        else if((arr[l]+arr[r])>X) r--;
        else l++;
    }
    return "No";
}

int main()
{
    int T,N,X;
    cin>>T;
    while(T--)
    {
        cin>>N>>X;
        int arr[N];
        for(int i=0;i<N;i++)
            cin>>arr[i];
        sort(arr,arr+N);
        cout<<pairSum(arr,N,X)<<endl;
    }
}
