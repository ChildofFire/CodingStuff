#include<bits/stdc++.h>
using namespace std;

class Node
{
public:
    bool visited;
    vector<int> adj;
    int distance;
    Node()
    {
        visited=false;
        distance=-1;
    }
};

void printShortestPaths(vector<Node> nodelist, int root)
{
    nodelist[root].visited=true;
    nodelist[root].distance=0;
    queue<int> levelqueue;
    levelqueue.push(root);
    while (!levelqueue.empty())
    {
        int curr=levelqueue.front();
        for (int i=0;i<nodelist[curr].adj.size();i++)
            if (!(nodelist[nodelist[curr].adj[i]].visited))
                {
                    levelqueue.push(nodelist[curr].adj[i]);
                    nodelist[nodelist[curr].adj[i]].visited=true;
                    nodelist[nodelist[curr].adj[i]].distance=nodelist[curr].distance+6;
                }
        levelqueue.pop();
    }
    for (int i=0;i<nodelist.size();i++)
        if (nodelist[i].distance)
            cout<<nodelist[i].distance<<" ";
    cout<<endl;
}

int main()
{
	int q;
	cin>>q;
	while(q--)
	{
		int n,m;
		cin>>n>>m;
		vector<Node> nodelist;
		while(n--)
        {
            Node newnode;
            nodelist.push_back(newnode);
        }
        while(m--)
        {
            int u,v;
            cin>>u>>v;
            nodelist[u-1].adj.push_back(v-1);
            nodelist[v-1].adj.push_back(u-1);
        }
        int root;
        cin>>root;
        root--;
        printShortestPaths(nodelist,root);

	}
}
