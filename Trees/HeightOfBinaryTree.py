class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def height(root): 
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
print("Height Of Tree: ", height(root))