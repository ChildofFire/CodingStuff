#include<iostream>
using namespace std;
 int main()
 {    long long int T,N,A[100000],B[100000],i,Amax,Bmax;
     cin>>T;
     while(T--)
     {
         cin>>N;
         for(i=0;i<N;i++)
            {cin>>B[i]; if(i==0) Bmax=B[i]; else if(Bmax<B[i]) Bmax=B[i];}
         for(i=0;i<N;i++)
            {cin>>A[i];  if(i==0) Amax=A[i]; else if(Amax<A[i]) Amax=A[i];}

       if(Bmax>Amax) cout<<"Bob"<<endl;
       else if(Amax>Bmax) cout<<"Alice"<<endl;
       else cout<<"Tie"<<endl;
     }


     return 0;
 }
