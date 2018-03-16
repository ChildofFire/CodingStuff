#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    long long int T,N,A[100000],i,c1,c2,counter=0,j;
    float median,tempmed;

    cin>>T;
    while(T--)
    {
        cin>>N;
        counter=0;
        if(N%2==0) {c1=N/2-1; c2=N/2;}
        else {c1=N/2; c2= N/2;}
        for(i=0;i<N;i++)
            cin>>A[i];

        sort(A,A+N);
        median=float((A[c1]+A[c2]))/2;

        for(i=0,j=N-1;i<=c1,j>=c2;i++,j--)
        {
            tempmed=float((A[i]+A[j]))/2;
            if(tempmed!=median) {counter++; break;}
        }

        if(counter==1)
            cout<<"NO"<<endl;
        else cout<<"YES"<<endl;
    }


    return 0;
}
