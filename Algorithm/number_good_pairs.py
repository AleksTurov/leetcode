class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i < j and num == num2:
                    good_pairs += 1
        return good_pairs

solution = Solution()
nums1 = [1,2,3,1,1,3]
print(solution.numIdenticalPairs(nums1))
