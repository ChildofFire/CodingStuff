#include<bits/stdc++.h>
using namespace std;

struct node
{
    int data;
    node *next;
};

class LL
{
    node *head; node *tail;
public:
    LL() { head=NULL; tail=NULL;}

    void createNode(int value)
    {
        if(head==NULL)
        {
            head=new node;
            head->data=value;
            head->next=NULL;
            tail=head;
        }
        else
        {
            node *temp=new node;
            temp->data=value;
            temp->next=NULL;
            tail->next=temp;
            tail=temp;
        }
    }

    void display()
    {
        if(head==NULL) cout<<"nothing to show!\n";
        else
        {
            node *temp=head;
            while(temp!=NULL)
            {
                cout<<temp->data<<endl;
                temp=temp->next;
            }
        }
    }
};

int main()
{
    LL linkList;
    for(int i=0;i<5;i++)
    {
        int value;
        cin>>value;
        linkList.createNode(value);
    }
    cout<<"here's the linked list: \n";
    linkList.display();
}
