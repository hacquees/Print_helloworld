"""Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
        a<=Number
        b<=Number 
        Means Increasing
"""
def increasingTriplet(nums):
    a=float('inf')
    b=float('inf')
    for i in nums:
        if i<=a:
            a=i
        elif i<=b:
            b=i
        else:
            return True

    return False

l=list(map(int,input().split()))
print(increasingTriplet(l))
