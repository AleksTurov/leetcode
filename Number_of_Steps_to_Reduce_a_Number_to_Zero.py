class Solution:
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num & 1:  # Проверяем, четное ли число (последний бит равен 1)
                num -= 1  # Если нечетное, вычитаем 1
            else:
                num >>= 1  # Если четное, сдвигаем биты вправо, что эквивалентно делению на 2
            steps += 1
        return steps

# Input
num = 14

solution = Solution()
steps = solution.numberOfSteps(num)
print(steps)
