class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        output = 0
        for operation in operations:
            if operation in ("--X", "X--"):
                output -= 1
            else:
                output += 1
        return output
solution = Solution()
operations = ["--X","X++","X++"]
print(solution.finalValueAfterOperations(operations))
