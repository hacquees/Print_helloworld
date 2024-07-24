# Sorting An Array in Incereasing order  Using MaxHeap 
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
        
def HeapSort(arr):
        # MaxHeap(arr,n)
        # if n>=0:
        #     arr[0],arr[n-1]=arr[n-1],arr[0]
        # for i in range(n-1,n//2,-1):
        #     HeapSort(arr,i)   #change Func definition ==> def HeapSort(arr,n)
        MaxHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            heapify(arr,i,0)
            
def HeapSortDesc(arr):
    MaxHeap(arr,n)
    for i in range(n-1,0,-1):
        heapify(arr,i,0)  
            
            
            
l=list(map(int,input().split()))  
n=len(l)
HeapSort(l)

print(*l)
HeapSortDesc(l)
print(*l)
