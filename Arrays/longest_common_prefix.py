class Solution:
    '''
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    '''
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]
        prefix = ''
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                prefix +=  first_str[i]
            else:
                break
        return prefix
    
# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""   