class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        first = second = third = float('-inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num < first:
                third = second
                second = num
            elif num > third and num < second:
                third = num
        if third != float('-inf'):
            return third
        else:
            return first

nums = [3, 2, 1, 3, 2]
solution = Solution()
result = solution.thirdMax(nums)
print("Result:", result) 