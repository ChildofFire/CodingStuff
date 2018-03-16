#include<bits/stdc++.h>
using namespace std;

bool isSubsetSum(int arr[], int n, int sum)
{
    bool mat[sum+1][n];

    for(int i=0;i<n;i++) mat[0][i]=true;
    for(int i=1;i<=sum;i++) mat[i][0]=false;
    mat[arr[0]][0]=true;
    for(int i=1;i<=sum;i++)
        for(int j=1;j<n;j++)
            if(i>=arr[j]) mat[i][j]=mat[i][j-1] || mat[i-arr[j]][j-1];
            else mat[i][j]=mat[i][j-1];

    return mat[sum][n-1];
 }

bool findPartition(int arr[], int n)
{
        int sum=0;
        for(int i=0;i<n;i++) sum+=arr[i];
        if(sum%2!=0) return false;
        else
            return isSubsetSum(arr,n,sum/2);
}

int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++) cin>>arr[i];
        if(findPartition(arr,n)) cout<<"YES";
        else cout<<"NO";
        cout<<endl;
    }
}
