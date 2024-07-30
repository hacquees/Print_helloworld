
def sortedSquares(nums):
    l=[0]*len(nums)
    i=0
    j=len(nums)-1
    k=len(nums)-1
    while i<=j:
        if abs(nums[i])>=abs(nums[j]):
            l[k]=nums[i]**2
            k-=1
            i+=1
        else:
            l[k]=nums[j]**2
            j-=1
            k-=1
    return (l)

print(*sortedSquares(list(map(int,input().split()))))
            
