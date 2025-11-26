from typing import List

class Solution:
    '''
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits  
        return [1] + [0] * len(digits)

# Example usage:
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]