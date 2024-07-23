class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.pre=None
        
        
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
            self.head.pre=self.tail
            self.tail.pre=self.head
        
        else:
            self.tail.next=newNode
            newNode.pre=self.tail
            self.tail=newNode
            self.tail.next=self.head
            self.head.pre=self.tail
            
            
    
    def traverseList(self):
        t=self.head
        while t!=self.tail:
            print("Current node",t.data,"Previous node",t.pre.data,"Next node",t.next.data)
            t=t.next
        print("Current node",t.data,"Previous node",t.pre.data,"Next node",t.next.data)

       
ll=LinkedList()
ll.insertAtLast(10)
ll.insertAtLast(20)
ll.insertAtLast(30)
ll.traverseList()