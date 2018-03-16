#include<bits/stdc++.h>
using namespace std;

int binSearch(int arr[], int X, int beg, int end)
{
    if(end>=beg)
    {
        int mid=beg+(end-beg)/2;
        if(X==arr[mid]) return mid;
        else if(X>arr[mid]) return binSearch(arr,X,mid+1,end);
        else return binSearch(arr,X,beg,mid-1);
    }
    return -1;
}

int revBinSearch(int arr[], int X, int beg, int end)
{
    if(end>=beg)
    {
        int mid=beg+(end-beg)/2;
        if(X==arr[mid]) return mid;
        else if(X>arr[mid]) return revBinSearch(arr,X,beg,mid-1);
        else return revBinSearch(arr,X,mid+1,end);
    }
    return -1;
}

int searchInBitonic(int arr[], int N, int X)
{
    int pivot;

    for(int i=0;i<N-1;i++)
    {
        if(arr[i]>=arr[i+1]) {pivot=i; break;}
    }

    if((X>=arr[0]) && (X<=arr[pivot]) )
        { int res=binSearch(arr,X,0,pivot);
            if(res==-1)
                {
                    if(X<=arr[pivot+1] && X>=arr[N-1])
                        return revBinSearch(arr,X,pivot+1,N-1);
                    else return -1;
                }
            else return res;

        }
    else if(X<=arr[pivot+1] && X>=arr[N-1])
                        return revBinSearch(arr,X,pivot+1,N-1);
    else return -1;
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
        {
            cin>>arr[i];
        }
        int res=searchInBitonic(arr,N,X);
        if(res==-1) cout<<"OOPS! NOT FOUND"<<endl;
        else cout<<res<<endl;
    }
    return 0;
}
