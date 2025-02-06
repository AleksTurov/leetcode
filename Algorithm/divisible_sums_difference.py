class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num2 = 0
        num1 = 0
        for i in range(n+1):
            if i != 0 and i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2
n = 10
m = 3

sol = Solution()
sol.differenceOfSums(n, m)
