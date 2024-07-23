class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        
n1=Node(11)
head=n1
n2=Node(12)
n3=Node(14)
n1.next=n2
n2.next=n3

t=head
while t:
    print(t.data)
    t=t.next 