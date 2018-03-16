#include<bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node* next;
};

class LL
{
    Node *head, *tail;
public:
    LL();
    void insertAtEnd(int);
    int deleteFromFront();
    //void display();
};

LL::LL()
{
    head=NULL;
    tail=NULL;
}
void LL::insertAtEnd(int value)
{
    Node *temp=new Node;
    temp->data=value;
    temp->next=NULL;
    if(head==NULL)
    {
        head=temp;
        tail=temp;
    }
    else
    {
        tail->next=temp;
        tail=temp;
    }
}

int LL::deleteFromFront()
{
    if(head==NULL) return -1;

    int val=head->data;
    head=head->next;
    return val;
}

/*void LL::display()
{
    Node *temp=head;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
}*/

void enqueue(LL *l1, int value)
{
    l1->insertAtEnd(value);
}
int dequeue(LL *l1)
{
    return l1->deleteFromFront();
}

int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        LL *l1=new LL;
        cin>>n;
        while(n--)
        {
            int choice;
            cin>>choice;
            if(choice==1)
            {
                int value;
                cin>>value;
                enqueue(l1,value);
            }
            else if(choice==2)
            {
                cout<<dequeue(l1)<<" ";
            }
        }
        delete(l1);
        cout<<endl;
    }
}
