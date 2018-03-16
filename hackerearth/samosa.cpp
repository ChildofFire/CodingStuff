#include<iostream>
#include<algorithm>>
using namespace std;
 int main()
 {   long long int N,K,c[1000],cost=0,i;
     cin>>N>>K;
     for(i=0;i<N;i++)
        cin>>c[i];
     sort(c,c+N);
     if(c[0]>K) cout<<0;
     else{

            for(i=0;i<N;i++)
            {
                cost+=c[i];
                if(cost>K) break;
            }

        cout<<i;
     }
     return 0;
 }
