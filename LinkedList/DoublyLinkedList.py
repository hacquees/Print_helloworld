class Node:
    def __init__(self,data) -> None:
        self.pre=None
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self) -> None:
        self.head=None
        
    def insertAtBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.pre=newNode
            self.head=newNode
    
    def insertAtLast(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            t= self.head
            
            while t.next:
                
                t=t.next
                
            t.next=newNode
            newNode.pre=t    
            
        print("Checking pre is connected or not",newNode.pre.data)
        
    def insertAtPos(self,pos,data):
        newNode=Node(data)
        if not self.head:
            print("Cant")
        if pos==0:
            newNode.next=self.head
            self.head.pre=newNode
            self.head=newNode
            
        else:
            i=0
            t=self.head
            while t and pos<i-1:
                t=t.next
                i+=1
            if not t:
                print("Not")
            newNode.next=t.next
            newNode.pre=t
            if t.next is not None:
                t.next.pre=newNode
            t.next=newNode
            
            #print(newNode.pre.data,newNode.next.data)
                    
    def insertAfterValue(self,v,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode    
        else:
            t= self.head
            while t:
                if t.data==v:
                    newNode.next=t.next
                    newNode.pre=t
                    if t.next:
                        t.next.pre=newNode
                    t.next=newNode  
                    
                    #print(newNode.pre.data,newNode.next.data)    next does not exist==>error
                    break
                
                t=t.next
                
            if  t is None:
                print("Cant not")
            
    def deleteAtBegin(self):
        if self.head is None:
            print("cant")
        elif self.head.next is None:
            self.head=None
            
        else:
            self.head=self.head.next
            self.head.pre=None
            
            
    def deleteAtLast(self):
        if self.head is None:
            print("cant")
        elif self.head.next is None:
            self.head=None
        else:
            t=self.head
            while t.next.next:
                t=t.next
                
            t.next=None
            
            # Second Method 
            
            # while t.next:
            #     t=t.next
                
            # t.pre.next=None
            
    def deleteAtPosition(self,pos):
        if self.head is None:
            print("cant")
        elif pos==0:
            self.head=self.head.next
            self.head.pre=None
        else:
            i=0
            t=self.head
            while t and i<pos-1:
                t=t.next
                i+=1
                
            if t is None :
                print("Cant")
                
            else:
                print(t.data)
                t.next=t.next.next
                if t.next: 
                    t.next.pre=t 
    
    def deleteByValue(self,v):
        if self.head is None:
            print("can't") 
        else:
            t=self.head
            while t:
                if t.data==v:
                    t.next.pre=t.pre
                    t.pre.next=t.next
                    break
                if t.next is None:
                    print("Cant")
                    break
                t=t.next        
                    
    def reverseList(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        while current:
            prev = current.pre
            current.pre = current.next
            current.next = prev
            current = current.pre
        if prev:
            self.head = prev.pre        
            
    def traverseList(self):
        t=self.head
        while t.next:
            print(t.data,end="<=>")
            t=t.next
        print(t.data)
            
ll=LinkedList()
ll.insertAtBegin(10)
ll.insertAtBegin(20)
ll.insertAtBegin(30)

ll.traverseList()
ll.insertAtLast(70)
ll.traverseList()
ll.insertAtPos(2,555)
ll.traverseList()
ll.insertAfterValue(20,644)
ll.traverseList()
print("After deleting first node")
ll.deleteAtBegin()
ll.traverseList()
ll.deleteAtLast()
print("After deleting last node")
ll.traverseList()
ll.deleteAtPosition(3)
print("After deleting postion node")

ll.traverseList()
ll.deleteByValue(20)
ll.traverseList()
ll.reverseList()
print("===============Reverse===============")
ll.traverseList()






