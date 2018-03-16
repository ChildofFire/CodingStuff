#include<bits/stdc++.h>
using namespace std;
int main()
{    map<string,int> team; vector<string> teamname;

    map<string,int> :: iterator iter;
    int N,i,max=-1;
    string s,t;
     cin>>N;
     for(i=0;i<N;i++)
     {

         cin>>s>>t;
         team[s]++; team[t]++;
     }

     for(iter=team.begin();iter!=team.end();iter++)
           if(iter->second>max)
                max=iter->second;

    for(iter=team.begin();iter!=team.end();iter++)
           if(iter->second==max) teamname.push_back(iter->first);

    sort(teamname.begin(),teamname.end());
    cout<<teamname.size()<<endl;
    for(i=0;i<teamname.size();i++)
      cout<<teamname[i]<<endl;
    return 0;
}
