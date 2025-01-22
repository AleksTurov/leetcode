class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num + t * 2

num = 4
t = 1
solution = Solution()
print(solution.theMaximumAchievableX(num, t))  # Ожидаемый вывод: 6