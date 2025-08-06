'''Given an array nums of integers, return how many of them contain an even number of digits

Example:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
'''
#Solution:

from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countDigit(num):
            c = 0
            while num != 0:
                num = num // 10
                c += 1
            return c

        count = 0
        for i in nums:
            x = countDigit(i)
            
            if x%2 == 0:
                count +=1 
            else:
                continue
        return count

s = Solution()
array = [12,345,2,6,7896]
count = s.findNumbers(array)
print(f"{count} numbers from {array} are Even didgit")