#Kadane's Algorithm
def maxSubArray(num):
    # a,b=nums[0],nums[0]
    # for i in range(1,len(nums)):
    #     if a>=0:
    #         a+=nums[i]
    #     else:
    #         a=nums[i]

    #     b=max(a,b)
        
    # return b

    best=-float('inf')
    ans=0
    for i in num:
        ans=max(ans+i,i)
        best=max(ans,best)
    return best

