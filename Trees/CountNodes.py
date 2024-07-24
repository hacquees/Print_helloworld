class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def count(root): 
    if root is None:
        return 0
    return count(root.left)+count(root.right)+1
        
# def count(root):
#     global c
#     if root:                   #if root is not None:
#         c+=1
#         count(root.left)
#         count(root.right)

                         
#c=0
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
# count(root)
#print("No. of nodes in a tree: ",c )
print("No of Nodes: ",count(root))