#include<bits/stdc++.h>
using namespace std;

void rotndel(long int arr[], int size, int nthlast)
{
    long int temp=arr[size-1];
    for(int i=size-1;i>0;i--)
        arr[i]=arr[i-1];
    arr[0]=temp;
    for(int i=size-nthlast;i<size-1;i++)
        arr[i]=arr[i+1];
}

int main()
{
    int T, N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        long int arr[N];
        for(int i=0;i<N;i++)
        cin>>arr[i];

        int j=1;
        for(int i=N;i>N/2;i--,j++)
        {
            rotndel(arr,i,j);
        }
        cout<<arr[0]<<endl;


    }
}
