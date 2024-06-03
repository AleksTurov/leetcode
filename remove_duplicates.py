class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = list(set(nums))
        unique_nums.sort()
        
        k = len(unique_nums)
        for i in range(k):
            nums[i] = unique_nums[i]
        
        return k

solution = Solution()
print(solution.removeDuplicates([1,1,2]))  
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))       