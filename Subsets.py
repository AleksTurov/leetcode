class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result

# Пример использования
solution = Solution()
print(solution.subsets([1, 2, 3]))  # Ожидаемый вывод: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(solution.subsets([0]))        # Ожидаемый вывод: [[], [0]]
