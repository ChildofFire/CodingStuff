#include<iostream>
#include<set>
using namespace std;
int main()
{ int a[]={0,9,56,5,0,5,5,5,0,0,0,3,3,4,0};
    typedef set<int> tyset;
tyset unique_set(a,a+15);

for (tyset::iterator iter = unique_set.begin(); iter != unique_set.end(); iter++)
    cout<<*iter<<" ";
    return 0;
}
