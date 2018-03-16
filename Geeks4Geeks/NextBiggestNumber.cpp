#include<bits/stdc++.h>
using namespace std;

string nextBiggest(int n)
{
    string digits,digits2;
    while(n>0)
    {
        char temp=48+n%10;
        digits+=temp;
        n/=10;
    }
    //cout<<"this is the first \"digits\": "<<digits<<endl;
    digits2=digits;
    sort(digits2.begin(),digits2.end());
    //cout<<"this is \"digits2\": "<<digits2<<endl;
    if(digits==digits2) return "not possible";
    //cout<<"this is \"digits\" after if: "<<digits<<endl;

    int i,j,counter=0;
    reverse(digits.begin(), digits.end());

    for(i=digits.length()-2;i>=0;i--)
        {
            for(j=digits.length()-1;j>i;j--)
                if(digits[j]>digits[i])
                {
                    char temp=digits[j];
                    digits[j]=digits[i];
                    digits[i]=temp;
                    counter++;
                    break;
                }
            if(counter) break;
        }
    //cout<<"this is original \"digits\": "<<digits<<endl;
    sort(digits.begin()+i+1,digits.end());
    return digits;
}

int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cout<<nextBiggest(n)<<endl;
    }
}
