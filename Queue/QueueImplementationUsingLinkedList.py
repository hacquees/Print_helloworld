class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        
    def Enqueue(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
            
    def Dequeue(self):
        if self.head is None:
            print("Can not be deleted b/c queue is empty")
        elif self.head.next is None:
            tempdata=self.head.data
            print("Deleted Element: ",tempdata)
            self.head=None
            self.tail=None
        else:
            tempdata=self.head.data
            print("Deleted Element: ",tempdata)
            self.head=self.head.next
            
    def Peak(self):
        if self.head is not None:
            print("Peak Value: ",self.head.data)
        else:
            print("Queue is Empty")
            
   
ll=LinkedList()
ll.Enqueue(10)
ll.Enqueue(20)
ll.Enqueue(30)
ll.Enqueue(40)
ll.Enqueue(50)
ll.Dequeue()
ll.Peak()
