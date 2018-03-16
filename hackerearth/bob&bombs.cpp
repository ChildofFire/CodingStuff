#include<iostream>
#include<set>
#include<string>
using namespace std;
int array[4000000];
 int main()
 {   long long int T,i,t,count,counter[10]={0};
    typedef set<int> tyset;
    string s;
   cin>>T;
for(t=0;t<T;t++)
         {count=0;
         cin>>s;
         s[s.length()+1]='C';
         for(i=0;i<s.length();i++)
         if(s[i]=='B') {array[count]=i-2; array[count+1]=i-1; array[count+2]=i+1; array[count+3]=i+2; count+=4;}

         tyset unique_set(array,array+count);

         for (tyset::iterator iter = unique_set.begin(); iter != unique_set.end(); iter++)
         {

             if(s[*iter]=='W') counter[t]++;
         }
 cout<<counter[t]<<endl;
         }



     return 0;
 }
