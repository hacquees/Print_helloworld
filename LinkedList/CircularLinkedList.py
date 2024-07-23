class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        
        
class LinkedList:
    def __init__(self) -> None:
        self.tail=None
        self.head=None
        
    def insertAtLast(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head
    def traverseList(self):
        t=self.head
        while t!=self.tail:
            print(t.data,end="<=>")
            t=t.next
        print(t.data)

ll=LinkedList()
ll.insertAtLast(10)
ll.insertAtLast(20)
ll.insertAtLast(30)
ll.traverseList()