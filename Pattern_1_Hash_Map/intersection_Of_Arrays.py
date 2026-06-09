'''Approach: Brute Force
To solve this problem, we can use a brute-force approach by iterating through both arrays and checking for common elements. We will create an empty list to store the unique common elements (intersection) and ensure that we do not add duplicates.
1. Initialize an empty list called result to store the unique common elements.
2. Iterate through each element i in the first array nums1.
   a. For each element i, iterate through each element j in the second array nums2.
   b. If i is equal to j and i is not already in the result list, add i to the result list. 
   3. After iterating through both arrays, return the result list containing the unique common elements.
   Time Complexity: O(n * m), where n is the length of nums1 and m is the length of nums2. We have to compare each element of nums1 with each element of nums2.
   Space Complexity: O(k), where k is the number of unique common elements in the result list. In the worst case, this could be O(min(n, m)) if all elements are common and unique. 
   '''

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in nums1:
            for j in nums2:
                if i == j and i not in result:
                    result.append(i)

        return result


result = Solution().intersection([1, 3, 2, 1], [2, 2,1])
print(result)  # Output: [2]
