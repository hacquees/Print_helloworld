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
    
    def minValue(self,root):
        t=root
        while t.left:
            t=t.left
            
        return t.data  
    
    def deleteNode(self,root,data):
        if root is None:
            return root
        if data<root.data:
            root.left=self.deleteNode(root.left,data)
        elif data> root.data:
            root.right=self.deleteNode(root.right,data)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp            
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=self.minValue(root.right)
            root.data=temp.data
            root.right=self.deleteNode(root.right,temp.data)
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
bst.deleteNode(root,30)
print()
bst.inOrder(root)
