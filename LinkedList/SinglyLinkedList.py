class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self) -> None:
        
        self.head=None
        
    def InsertAtBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
            
    def InserAtLast(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            t=self.head
            while t.next:
                t=t.next
                
            t.next=newNode
            
    def InsertAtPosition(self,data,pos):
        newNode=Node(data)
        
        if self.head is None:
            self.head=newNode
            
        else:
            """ t=self.head
            while pos and t:
               p=t
               t=t.next
               pos-=1
            if p.next:              
                p.next=newNode
                newNode.next=t
            else:
                print("Cant") """
                
            t=self.head
            i=0
            while t and i<pos-1:
                t=t.next
                i+=1
                
            if t is None:
                print("CANt")
            else:
                newNode.next=t.next
                t.next=newNode
            
    def traverseList(self):
        t=self.head
        while t.next:
            print(t.data,end="=>")
            t=t.next
        print(t.data)
        
    def countNode(self):
        t=self.head
        c=0
        while t:
            c+=1
            t=t.next
            
        print("Count = ",c)
        
    def maxValue(self):
        t=self.head
        mx= -float('inf')
        if t is None:
            print("No max")
        else:
            while t:
                mx=max(t.data,mx)
                t=t.next
                
            print("Maximum Value = ",mx)
    def insertAfterValue(self,v,data):
        newNode=Node(data)
        if self.head is None:
            print("Can't")
        t=self.head
        while t:
            if t.data==v:
                newNode.next=t.next
                t.next=newNode
                break
                
            if t.next is None:
                print("Cant'")
                break
            t=t.next
            
    def deleteAtBegin(self):
        if self.head is None:
            print("cant")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            
            
    def deleteAtLast(self):
        if not self.head:
            print("cant")
        elif self.head.next is None:
            self.head=None
        else:
            t=self.head
            while t.next.next:
                t=t.next
            t.next=None
        
    def deleteAtPosition(self,pos):
    
        if self.head is None:
            print("Can't")
        elif pos==0:
            self.head==self.head.next
            
        else:
            i=0
            t=self.head
            while t and i<pos-1:
                t=t.next
                i+=1
                
            if t is None:
                print("Can't")
            else:
                t.next=t.next.next
                
                
    def deleteByValue(self,v):
        if self.head is None:
            print("Can't")
            
        elif self.head.data==v:
            self.head=self.head.next
        else:
            t=self.head
            while t:
                if t.next.data==v:
                    t.next=t.next.next
                    break
                if t.next :
                    print("Cant")
                    break
                t=t.next
                
    def reverseList(self):
        """ Use 3 Pointter change  => to <=  """
        
        pre=None
        curr=self.head
            
        while curr:
            n=curr.next
            curr.next=pre
            pre=curr
            curr=n
        self.head=pre 
                
                
ll=LinkedList()
ll.InsertAtBegin(10)
ll.InsertAtBegin(20)
ll.InsertAtBegin(30)
ll.InserAtLast(40)
ll.InsertAtPosition(69,2)
ll.insertAfterValue(20,500)
# ll.traverseList()
# print("========================")

# ll.deleteAtBegin()
# ll.traverseList()
# ll.countNode()
# ll.maxValue()
# ll.traverseList()
# print("========================")

# ll.deleteAtLast()
# ll.traverseList()
# ll.deleteAtPosition(2)
# ll.traverseList()
# print("By value deletion")
# ll.deleteByValue(20)
ll.traverseList()

ll.reverseList()
ll.traverseList()


