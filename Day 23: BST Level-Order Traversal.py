#Welcome to BST World
import sys
#Cretaing nOde Class
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
#Create Solution for tree! Thw blue print of an object
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = [root]
        while len(queue) is not 0:
            cur = queue[0]
            queue=queue[1 :]
            print(cur.data,end=" ")
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        
T=int(input())
#myTree object
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
