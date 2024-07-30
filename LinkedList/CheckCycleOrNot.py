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
def Cycle():
    # t=head
    # l=[]    
    # while t:
    #     if t in l:
    #         return True
    #     else:
    #         l.append(t)
    #     t=t.next
    # return False  
    
    # Using Two Pointer
    
    if  head is None or head.next is None :
            return False
    i=head
    j=head
    while j and j.next:
        
        i=i.next
        j=j.next.next
        if i==j:
            return True

    return False
 
            
ll=LinkedList()
n1=Node(1)
head=n1
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n2
print(Cycle())