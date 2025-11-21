import pandas as pd
from typing import List

class Solution:
    '''
    Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 
    If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 
    Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
    '''
 
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        cur = 0
        
        for i, x in enumerate(nums):
            cur += x
            if cur > total - cur:
                return nums[:i+1]
# Example usage:    
nums = [4,3,10,9,8]
solution = Solution()
result = solution.minSubsequence(nums)
print(result)  # Output: [10,9]