#include<bits/stdc++.h>
using namespace std;
int main()
{

    int T,N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        int a[N],pos[N],neg[N],poscount=0,negcount=0;
        for(int i=0;i<N;i++)
        {
            cin>>a[i];
            if(a[i]>=0) pos[poscount++]=a[i];
            else neg[negcount++]=a[i];
        }
        int min; string more;
        if(poscount>negcount) {min=negcount; more="pos";}
        else {min=poscount; more="neg";}
        for(int i=0;i<min;i++)
        {
            cout<<pos[i]<<" "<<neg[i]<<" ";
        }
        if(more=="neg") {for(int i=min;i<N-min;i++) cout<<neg[i]<<" ";}
        else if(more=="pos") {for(int i=min;i<N-min;i++) cout<<pos[i]<<" ";}
        cout<<endl;
    }
}
