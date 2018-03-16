//Program to return the path sum of the longest path in a binary tree.
//If many longest paths exist, then returns the one with max path sum.

#include<bits/stdc++.h>
using namespace std;

struct Node
{
    int data; Node *left, *right;
};

Node* createNode(int value)
{
    Node *temp=new Node;
    temp->data=value;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
}

vector<pair<int,int> > pathmap;         //vector of pairs to hold values of pathlen and pathsum resp.

void populateMap(Node *node, int pathlen, int sum)      //function to populate pathmap
{
    if(node==NULL) return;

    if(node->left==NULL && node->right==NULL)
        pathmap.push_back(make_pair(pathlen,sum+node->data));
    else
    {
        populateMap(node->left,pathlen+1,sum+node->data);
        populateMap(node->right,pathlen+1,sum+node->data);
    }
}


int longestPathSum(Node *node)
{
    populateMap(node,0,0);
    if(pathmap.size()==0) return 0;

    int maxlen=0;
    vector<pair<int,int> >::iterator i;
    for(i=pathmap.begin();i<pathmap.end();i++)
    {
        if(maxlen<i->first) maxlen=i->first;
    }
    int maxsum=0;
    for(i=pathmap.begin();i<pathmap.end();i++)
    {
        if(maxlen== i->first && maxsum< i->second) maxsum=i->second;
    }

    return maxsum;
}

int main()
{
    Node *root=createNode(1);
    Node *leftOfRoot=createNode(2);
    Node *rightOfRoot=createNode(3);
    Node *leftOfRightOfRoot=createNode(18);
    Node *rightOfRightOfRoot=createNode(5);
    root->left=leftOfRoot;
    root->right=rightOfRoot;
    root->right->left=leftOfRightOfRoot;
    root->right->right=rightOfRightOfRoot;

    pathmap.clear();

    cout<<longestPathSum(root)<<endl;

}
