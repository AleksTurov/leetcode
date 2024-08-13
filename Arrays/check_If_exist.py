class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        
        return False

print(Solution().checkIfExist([10, 2, 5, 3])) 
print(Solution().checkIfExist([1, 2, 3, 4]))
print(Solution().checkIfExist([7, 1, 14, 11])) 
print(Solution().checkIfExist([3, 1, 7, 11])) 
