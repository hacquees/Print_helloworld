class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def maximum(root): 
    if root is None:
        return 0 
    max_left=maximum(root.left)
    max_right=maximum(root.right)
    return max(max_right,max_left,root.data)

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
print("Maximum Element: ", maximum(root))