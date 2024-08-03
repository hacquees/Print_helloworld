"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105"""


def containsNearbyDuplicate(nums, k):
    i=0
    j=0
    s=set()
    while j<len(nums):
        if abs(i-j)>k:              #Shrink
            s.remove(nums[i])
            i+=1

        if nums[j] in s:            #Is In Given Window
            return True
        s.add(nums[j])
        j+=1
    return False

k=int(input())
nums=list(map(int,input().split()))
print(containsNearbyDuplicate(nums,k))