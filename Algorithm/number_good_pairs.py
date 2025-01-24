class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        good_pairs = 0
        
        for num in nums:
            good_pairs += count[num]
            count[num] += 1
        
        return good_pairs

solution = Solution()   
print(solution.numIdenticalPairs([1,2,3,1,1,3])) # 4
print(solution.numIdenticalPairs([1,1,1,1])) # 6
print(solution.numIdenticalPairs([1,2,1,1,2])) # 4