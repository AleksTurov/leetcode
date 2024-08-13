class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1


                
        return left


solution = Solution()
print(solution.removeElement(nums = [3,2,2,3], val = 3))  
print(solution.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)  )

