def prefixes(text):
	return [text[0:i] for i in range(1,len(text)+1)]

contact_dic={}
def add(text):
	for i in prefixes(text):
		contact_dic[i]=contact_dic.get(i,0)+1

def find(text):
	return contact_dic.get(text,0)


for i in range(int(input())):
	query=input().split()
	if query[0]=='add':
		add(query[1])
	elif query[0]=='find':
		print(find(query[1]))
