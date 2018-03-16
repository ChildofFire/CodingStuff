#include<bits/stdc++.h>
using namespace std;

struct Node
{
    int data; Node *next;
};

Node* createNode(int value)
{
    Node* temp=new Node;
    temp->data=value;
    temp->next=NULL;
    return temp;
}

void display(Node* node)
{
    if(!node) return;
    cout<<node->data<<" ";
    display(node->next);
}

void reverseList(Node *node)
{
    if(!node) return;

    vector<int> temp;
    Node *tempNode=node;
    while(tempNode)
    {
        temp.push_back(tempNode->data);
        tempNode=tempNode->next;
    }
    //tempNode=node;
    for(int i=temp.size()-1;i>-1;i--)
    {
        node->data=temp[i];
        node=node->next;
    }
}

int main()
{
    Node *head=createNode(0);
    Node *first=createNode(1);
    Node *second=createNode(2);
    head->next=first;
    first->next=second;
    display(head);
    cout<<endl;
    reverseList(head);
    display(head);
}
