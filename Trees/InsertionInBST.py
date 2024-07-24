#Insertion in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Bst:        
    def insertNode(self,root,data):
        if root is None :
            return Node(data)
        elif root.data>data:
            root.left=self.insertNode(root.left,data)
        else: 
            root.right =self.insertNode(root.right,data)
        return root
    
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data,end=" ")
            self.inOrder(root.right)
            
bst=Bst() 
root=None
root=bst.insertNode(root,20)
root=bst.insertNode(root,30)
root=bst.insertNode(root,40)
root=bst.insertNode(root,80)
root=bst.insertNode(root,7)
root=bst.insertNode(root,9)

bst.inOrder(root)