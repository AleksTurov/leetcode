class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1 
            if nums[index] > 0:  
                nums[index] = -nums[index]
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  
print(solution.findDisappearedNumbers([1,1])) 
