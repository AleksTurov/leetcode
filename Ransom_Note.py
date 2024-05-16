class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import defaultdict
        
        magazine_count = defaultdict(int)
        for char in magazine:
            magazine_count[char] += 1
        
        for char in ransomNote:
            if magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1
        
        return True

ransomNote = "aa" 
magazine = "aab"
solution = Solution()
print(solution.canConstruct(ransomNote, magazine)) 
