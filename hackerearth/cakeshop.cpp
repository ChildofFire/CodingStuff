#include<iostream>
#include<cmath>
using namespace std;
int main()
{

long long int X,k,i,remain;
    cin>>X;

    k=ceil(pow(3*X,0.333333));

    for(i=k;i>=1;i--)
        if((i*(i+1)*(i+2)/3)<=X) break;

    remain=X-i*(i+1)*(i+2)/3;

    if((remain==0)||(remain>(i+1)))
        cout<<"Chandan";
    else
        cout<<"Darshak";

    return 0;
}
