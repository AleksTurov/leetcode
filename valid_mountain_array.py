class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        
        max_index = arr.index(max(arr))
        if max_index == 0 or max_index == n - 1:
            return False
        
        for i in range(1, max_index + 1):
            if arr[i] <= arr[i - 1]:
                return False
        
        for i in range(max_index + 1, n):
            if arr[i] >= arr[i - 1]:
                return False
        
        return True
                  



solution = Solution()
print(solution.validMountainArray(arr = [3,2,2,3]))  
print(solution.validMountainArray(arr = [0,3,2,1]))