class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        nums2 = []
        for num in arr:
            if num != 0:
                nums2.append(num)
            else:
                nums2.append(num)
                nums2.append(num)
        
        for i in range(len(arr)):
            arr[i] = nums2[i]
        return arr

arr = [1,0,2,3,0,4,5,0]

solution = Solution()
out = solution.duplicateZeros(arr)

print(out)