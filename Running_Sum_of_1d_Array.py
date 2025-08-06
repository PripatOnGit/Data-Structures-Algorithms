'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i,num in enumerate(nums):
            if i==0:
                nums[i] = num
            else:
                nums[i] = num + nums[i-1]
        return nums
    
s = Solution()
arr = [1,2,3,4]
arr = s.runningSum(arr)
print(arr)