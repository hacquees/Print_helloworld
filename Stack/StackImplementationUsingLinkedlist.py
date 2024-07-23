class Node:
    def __init__(self,data) -> None:
        self.next=None
        self.data=data
        
class LinkedList:
    def __init__(self,l) -> None:
        self.head=None
        self.count=0
        self.length=l
        
    def push(self,ele):
        newNode=Node(ele)
        if self.count<=self.length:
            if self.head is None:
                self.head=newNode
                self.count+=1
                
            else:
                newNode.next=self.head
                self.head=newNode
                self.count+=1
        else:
            print("OverFlow")
            
    def pop(self):
        if self.head is None:
            print("Underflow")
        else:
            print("Deleted Element: ",self.head.data)
            self.head=self.head.next
            self.count-=1
            
    def peak(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            print("Peak Element: ", self.head.data)
    
    def traverseList(self):
        t=self.head
        while t.next:
            print(t.data,end="=>")
            t=t.next
        print(t.data)
            
ll=LinkedList(5)
ll.push(10)
ll.push(20)
ll.push(30)
ll.pop()
ll.peak()
ll.traverseList()   
            