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
    arr=l
    n=len(arr)
    if n==0:
        arr.append(data)
    else:
        arr.append(data)
        MaxHeap(arr,n)
        # for i in range(n//2-1,-1,-1):
        #     heapify(arr,n,i)
             
def Delete(arr,num):
    n=len(arr)
    arr.remove(num)
    MaxHeap(arr,n)
    # for i in range(n//2-1,-1,-1):
    #         heapify(arr,n,i)     
    

l=[]
Insert(3)  
Insert(12)
Insert(11)
Insert(7)
Insert(9)
Insert(15)
Insert(2)
print(*l)