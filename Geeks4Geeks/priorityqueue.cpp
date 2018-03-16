#include<bits/stdc++.h>
using namespace std;
int main()
{
	priority_queue<int> q;
	q.push(7);
	q.push(10);
	q.push(11);
	q.push(12);
	q.push(13);
	queue<int> q2;
	q2.push(7);
	q2.push(6);
	q2.push(4);
	q2.push(1);
	q2.push(5);

	while(!q.empty())
        {int n=q.top(), m=q2.front();
        	q.pop(); q2.pop();
        	cout<<n<<" "<<m<<endl;
}
}
