#include<iostream>
#include<cmath>
using namespace std;
 int main()
 {   long int T,N,D,i,a[1000],counter;
     cin>>T;
     while(T--)
     {

         counter=0;
         cin>>N>>D;
         for(i=0;i<N;i++)
            cin>>a[i];

         for(i=0;i<N;i++)
           if(i>0)
           if(abs(a[i]-a[i-1])>D) {counter++; break;}


        if(counter==1) cout<<"NO";
        else cout<<"YES";
     }
     return 0;
 }
