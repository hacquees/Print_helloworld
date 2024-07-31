def moveZeroes( nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    # i=0
    # for j in range(len(nums)):
    #     if nums[j]:
    #         nums[i]=nums[j]
    #         i+=1
        

    # for i in range(i,len(nums)):
    #     nums[i]=0
    # return nums
    
    i=0
    for j in range(len(nums)):
        if nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1

    return nums

print(*moveZeroes(list(map(int,input().split()))))
