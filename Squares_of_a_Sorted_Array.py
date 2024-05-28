class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = []
        for num in nums:
            num2 = num ** 2
            nums2.append(num2)
        nums2.sort()
        return nums2

nums = [-4,-1,0,3,10]
solution = Solution()
sortedSquares = solution.sortedSquares(nums)

print(sortedSquares)