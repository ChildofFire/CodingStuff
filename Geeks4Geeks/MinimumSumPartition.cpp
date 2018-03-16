#include<bits/stdc++.h>
using namespace std;

int minSum(int arr[], int n)
{
    int sum=0;
    for(int i=0;i<n;i++) sum+=arr[i];
    bool dp[sum/2+1][n+1];
    for(int j=0;j<=n;j++) dp[0][j]=true;
    for(int i=1;i<=sum/2;i++) dp[i][0]=false;

    int maxsum=0;

    for(int i=1;i<=sum/2;i++)
        for(int j=1;j<=n;j++)
            {
                dp[i][j]=dp[i][j-1];
                if(i>=arr[j-1]) dp[i][j] = dp[i][j] || dp[i-arr[j-1]][j-1];
                if(j==n && dp[i][j]==true) maxsum=abs(2*i-sum);
            }

    return maxsum;
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
        cout<<minSum(arr,n)<<endl;
    }
}
