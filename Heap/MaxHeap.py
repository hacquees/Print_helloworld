def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    
    if left<n and arr[largest]<arr[left]:
        largest=left
    if right<n and  arr[largest]<arr[right]:
        largest=right
        
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
  
def MaxHeap(arr,n):
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

def Insert(data):
    if len(l)==0:
        l.append(data)
    else:
        n=len(l)
        l.append(data)
        for i in range(len(l)//2-1,-1,-1):
            heapify(l,len(l),i)
             
def Delete(num):
    l.remove(num)
    for i in range(len(l)//2-1,-1,-1):
            heapify(l,len(l),i)
    

l=[]
Insert(3)
Insert(12)
Insert(11)
Insert(7)
Insert(9)
Insert(15)
Insert(2)
Insert(155)
print(*l)
Delete(12)
print(*l)