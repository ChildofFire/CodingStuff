#include<bits/stdc++.h>
using namespace std;
int main()
{   map<string,int> Brand;  vector<string> Brandname;
    map<string,int>::iterator iter;
    int max=-1,N;
    string s;
    cin>>N;
    for(int i=0;i<N;i++)
    {

        cin>>s;
            Brand[s]++;


    }

    for(iter=Brand.begin();iter!=Brand.end();iter++)
           if(iter->second>max)
                max=iter->second;

    for(iter=Brand.begin();iter!=Brand.end();iter++)
           if(iter->second==max) Brandname.push_back(iter->first);

    sort(Brandname.begin(),Brandname.end());
    cout<<Brandname[0]<<endl;
    return 0;
}
