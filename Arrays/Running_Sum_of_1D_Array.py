class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for j in range(1, len(nums)):
            nums[j] = nums[j] + nums[j - 1]
            
        return nums

solution = Solution()
nums = [1,2,3,4]
nums = [1,1,1,1,1]
nums = [3,1,2,10,1]

out = solution.runningSum(nums)
print(out)



