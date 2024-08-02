"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""


def minSubArrayLen(target,nums):
    i=0
    j=0
    s=0
    start=0
    l=float('inf')
    while j<len(nums):
        if s<target:
            s+=nums[j]
    
        while s>=target:
            if j-i+1<l:
                l=j-i+1
    
            s=s-nums[i]
        
            i+=1

        j+=1

    if l==float('inf'):
        return 0
    return l

target=int(input())
nums=list(map(int,input().split()))
print(minSubArrayLen(target,nums))
        