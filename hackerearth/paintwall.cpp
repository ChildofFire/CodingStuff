#include<iostream>
using namespace std;
long long int ans[100000],modulo=1000000007,i,T,N;
 int main()
 {

     ans[0]=3;
     for(i=1;i<=100000;i++)
        ans[i]=(ans[i-1]*2)%modulo;
     cin>>T;
     while(T--)
     {
         cin>>N;
         cout<<ans[N-1]<<endl;
     }

     return 0;
 }
