class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
        
class AVLTree:
    def height(self,node):
        if node is None:
            return 0
        else:      
            return node.height
        
    def balance(self,node):
        if node is node:
            return 0
        return self.height(node.left)-self.height(node.right)
    
    def minValue(self,root):
        t=root
        while root.left:
            t=t.left
        return t
    
    def insert(self,root,data):
        if not root:
            return Node(data)
        elif root.data>data:
            root.left=self.insert(root.left,data)
        else: 
            root.right =self.insert(root.right,data)
        
        # Increasing height after Insertion     
        root.height=1+max(self.height(root.left),self.height(root.right))
        
        # Checking Balance Factor
        balance=self.balance(root)
        
        # LL Rotation
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)
        
        # RR Rotation
        if balance < -1 and data  > root.right.data:
            return self.left_rotate(root)
 
         # LR Rotation
        if balance > 1 and data > root.left.data:
            root.left =self.left_rotate(root.left)
            return self.right_rotate(root)
 
         # RL Rotation
        if balance < -1 and data < root.right.data:
            root.right =self.right_rotate(root.right)
            return self.left_rotate(root)
       
        return root
        
    def delete(self,root,data):
        if not root:
            return root
        if data < root.data:
            self.left=self.delete(root.left,data)
        elif data > root.data:
            self.right = self.delete(root.right,data)
        else:
            if root.left is None:
                t=root.right
                root=None
                return t
            elif root.right is None:
                t=root.left
                root=None
                return t
            t=self.minValue(root.right)
            root.data=t.data
            root.right=self.delete(root.right,t.data)
        
        if root is  None:
            return root
         # Increasing height after Insertion     
        root.height=1+max(self.height(root.left),self.height(root.right))
        
        # Checking Balance Factor
        balance=self.balance(root)
        
        # LL Rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)
        
        # RR Rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)
 
         # LR Rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left =self.left_rotate(root.left)
            return self.right_rotate(root)
 
         # RL Rotation
        if balance < -1 and self.balance(root.left) > 0 :
            root.right =self.right_rotate(root.right)
            return self.left_rotate(root)
       
        return root
        
        
        
        
        """
                    x                                         y
                   / \                                       / \                                                                                  
                  /   \                                     /   \
                 y     t3  ==> After Right Rotate==>      t1     x
                / \        <== After Left Roatate<==            / \
               /   \                                           /   \
             t1    t2                                         t2   t3 

        """ 
    def left_rotate(self,y):
        x=y.right
        t2=x.left
        x.left=y
        y.right=t2
        x.height=1+max(self.height(x.left),self.height(x.right))
        y.height=1+max(self.height(y.left),self.height(y.right))
        return x


    def right_rotate(self,x):
        y=x.left
        t2=x.right
        y.left=x
        x.left=t2
        x.height=1+max(self.height(x.left),self.height(x.right))
        y.height=1+max(self.height(y.left),self.height(y.right))
        return x
    
    
    def traverse(self,root):
        if root:
            self.traverse(root.left)
            print(root.data,end=" ")
            self.traverse(root.right)        
        
        
avl = AVLTree()
root = None
root = avl.insert(root,10)
root = avl.insert(root,20)
root = avl.insert(root,30)
root = avl.insert(root,40)
root = avl.insert(root,50)
root = avl.insert(root,25)
avl.traverse(root)
avl.delete(root,30)
print("\nAfter Deletion")
avl.traverse(root)

