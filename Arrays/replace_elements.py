class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        1 <= arr.length <= 104
        1 <= arr[i] <= 105
        """
        
        if len(arr) == 1:
            return [-1]
        elif len(arr) <1:
            return None
                   
        right = len(arr) - 1

        max_from_right = -1

        for i in range(right, -1, -1):
            new_val = max_from_right

            if arr[i] > max_from_right:
                max_from_right = arr[i]
            
            arr[i] = new_val
            print(arr)
        return arr


solution = Solution()
print(solution.replaceElements(arr = [400]))  
print(solution.replaceElements(arr = [0,1,2,2,3,0,4,2]))

