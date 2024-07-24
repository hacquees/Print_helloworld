# Sorting An Array in Decereasing order  Using MinHeap 
def heapify(arr,n,i):
    smallest=i
    left=2*i+1
    right=2*i+2
    
    if left<n and arr[smallest]>arr[left]:
        smallest=left
    if right<n and  arr[smallest]>arr[right]:
        smallest=right
        
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapify(arr,n,smallest)
  
def MinHeap(arr,n):
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
        
def HeapSort(arr,n):
        MinHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            heapify(arr,i,0)
            

l=list(map(int,input().split()))  
HeapSort(l,len(l))
print(*l)