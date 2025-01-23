class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')

address = "1.1.1.1"
solution = Solution()
print(solution.defangIPaddr(address))