import pandas as pd
from typing import List

class Solution:
    ''' 
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)             
# Example usage:
solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))  # Output: 2
print(solution.searchInsert([1,3,5,6], 2))  # Output: 1
print(solution.searchInsert([1,3,5,6], 7))  # Output: 4
print(solution.searchInsert([1,3,5,6], 0))  # Output: 0
print(solution.searchInsert([], 5))         # Output: 1
            
        