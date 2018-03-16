#include<bits/stdc++.h>
using namespace std;

int rotateByD(int arr[], int size, int d)
{
    int temp[d];
    for(int i=0;i<d;i++)
        temp[i]=arr[i];
    for(int i=0;i<size-d;i++)
        arr[i]=arr[i+d];
    for(int i=size-d;i<size;i++)
        arr[i]=temp[i-size+d];

}

int main()
{
    int T,N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        int arr[N],d;
        for(int i=0;i<N;i++)
            cin>>arr[i];
        cin>>d;
        rotateByD(arr,N,d);
        for(int i=0;i<N;i++)
            cout<<arr[i]<<" ";
        cout<<endl;
    }
}
