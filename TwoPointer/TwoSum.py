def twoSum(numbers,target):
    i=0
    j=len(numbers)-1
    while i<j:
        if (numbers[i]+numbers[j])==target:
            return [i+1,j+1]
        if (numbers[i]+numbers[j])>target:
            j-=1
        if (numbers[i]+numbers[j])<target:
            i+=1
            

target=int(input())
numbers=list(map(int,input().split()))
print(twoSum(numbers,target))