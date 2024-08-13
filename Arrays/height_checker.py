class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        expected = sorted(heights)

        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count

heights = [1,1,4,2,1,3]

solution = Solution()
result = solution.heightChecker(heights)

print(result) 