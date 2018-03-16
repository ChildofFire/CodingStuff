#include<bits/stdc++.h>
using namespace std;

struct Box
{
    int l, b, h;
};

int max(int a, int b)
{
    return (a>=b)? a:b;
}

int min(int a, int b)
{
    return (a<b)? a:b;
}

int compareBox(const void *b1, const void *b2)
{
    int res=(*(Box*)b2).l*(*(Box*)b2).b - (*(Box*)b1).l*(*(Box*)b1).b;
    return res;
}

int maxHeight(Box arr[], int n)
{
    Box rotations[3*n]; int index=0;
    for(int i=0;i<n;i++)
        {
            rotations[index]=arr[i];
            index++;

            rotations[index].h=arr[i].l;
            rotations[index].l=max(arr[i].h, arr[i].b);
            rotations[index].b=min(arr[i].h,arr[i].b);
            index++;

            rotations[index].h=arr[i].b;
            rotations[index].l=max(arr[i].l, arr[i].h);
            rotations[index].b=min(arr[i].l, arr[i].h);

            index++;
        }
    n*=3;
    qsort(rotations, n,sizeof(rotations[0]),compareBox);
    int max_height[n];
    for(int i=0;i<n; i++) max_height[i]=rotations[i].h;

    for(int i=1;i<n;i++)
        for(int j=0;j<i;j++)
            if(rotations[i].l<rotations[j].l && rotations[i].b<rotations[j].b && max_height[i] < max_height[j]+rotations[i].h)
                max_height[i]=max_height[j]+rotations[i].h;
    int max_stack_height=max_height[0];
    for(int i=1;i<n;i++)
        if(max_height[i]>max_stack_height) max_stack_height=max_height[i];

    return max_stack_height;
}
int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        Box arr[n];
        for(int i=0;i<n;i++) cin>>arr[i].l>>arr[i].b>>arr[i].h;
        cout<<maxHeight(arr,n)<<endl;
    }
}
