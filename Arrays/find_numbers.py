class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_even_digits = 0
        
        for num in nums:
            if len(str(num)) % 2 == 0:
                count_even_digits += 1
                
        return count_even_digits

nums = [12,345,2,6,7896]
solution = Solution()
findNumbers = solution.findNumbers(nums)

print(findNumbers)