class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            else:
                current_count = 0
        
        return max_count

nums = [1,1,0,1,1,1]
solution = Solution()
max_count = solution.findMaxConsecutiveOnes(nums)

print(max_count)