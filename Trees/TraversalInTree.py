class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)
        
def preOrder(root):
    if root:
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right) 
        
def postOrder(root):
    if root:
        preOrder(root.left)
        preOrder(root.right)   
        print(root.data,end=" ")  
        
def levelOrder(root):
    if not root:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

                               
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
print("Inorder:",end=" ")
inOrder(root)
print("\nPreOrder:",end=" ")
preOrder(root)
print("\nPostOrder",end=" ")
postOrder(root)
print("\nLevelOrder",end=" ")
levelOrder(root)
