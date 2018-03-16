import heapq
list1=[5,7,9,1,3]
list2=[x for x in list1]
print("original list: \n",list1)
heapq.heapify(list1)
print ("list after being minheaped:\n",list1)
print ("list before being maxheaped:\n",list2)
heapq._heapify_max(list2)
print("list after being maxheaped: \n",list2)