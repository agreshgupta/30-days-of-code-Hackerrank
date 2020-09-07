#creating a node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    #inserting fuction
    def insert(self,head,data): 
        newNode = Node(data)
        if head == None:
            return newNode
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next=newNode
        return head
        
   
#declaring mylist and coping solution class to it
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	 
