#include<bits/stdc++.h>
using namespace std;

class TrieNode
{
public:
    TrieNode* children[26];
	int visits;
	TrieNode()
	{
		for (int i=0;i<26;i++)
			children[i]=NULL;
		visits=0;
	}
};

class Trie
{
	TrieNode* root=new TrieNode();
public:
	void insert(string s)
	{
		root->visits++;
		TrieNode* crawler=root;
		for(int i=0;i<s.length();i++)
		{
			if(!crawler->children[s[i]-'a'])
                crawler->children[s[i]-'a']=new TrieNode();
			crawler=crawler->children[s[i]-'a'];
			crawler->visits++;
		}
	}

	int patternCount(string s)
	{
		TrieNode* crawler=root;
		for(int i=0;i<s.length();i++)
		{
			if(!crawler->children[s[i]-'a']) return 0;
			crawler=crawler->children[s[i]-'a'];
		}
		return crawler->visits;
	}
};
int main()
{
	Trie* trie=new Trie();
	int t;
	cin>>t;
	while(t--)
	{
		string choice;
		cin>>choice;
		string s;
		if(choice=="add")
		{
					cin>>s;
					trie->insert(s);
		}
		else
		{
					cin>>s;
					cout<<trie->patternCount(s)<<"\n";
		}

	}
	return 0;
}