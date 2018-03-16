#include<iostream>
using namespace std;

long long int A[1000000],counter[100000000]={0};
int main()
{   long long int N,i,big,unique=-1;
    cin>>N;
    for(i=0;i<N;i++)
    {   cin>>A[i];
        if(i==0) big=A[i];
        else if(big<A[i]) big= A[i];
         counter[A[i]]++;
    }



    for(i=big;i>=0;i--)
    {
            if(counter[i]==1) {unique=i; break;}
    }


    cout<<unique<<endl;

    return 0;
}
