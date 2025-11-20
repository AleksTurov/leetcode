import pandas as pd
from typing import List

class Solution:
    '''
    Given a circular array nums, find the maximum absolute difference between adjacent elements.
    Note: In a circular array, the first and last elements are adjacent.
    '''
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        dif = abs(nums[0] - nums[-1])
        dif_temp=dif
        for i in range(len(nums)):
            dif_temp = abs(nums[i] - nums[i-1])
            if dif_temp > dif:
                dif = dif_temp
        return dif 

print(Solution().maxAdjacentDistance([1,2,4]))  # Output: 3
print(Solution().maxAdjacentDistance([-5,-10,-5]))    # Output: 5

# Time Complexity: O(n)
# Space Complexity: O(1)