class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        j = 0
        for i in range(len(words)):
            if words[i].startswith(pref):
                j += 1
        return j
 

pref = "at"
words = ["pay","attention","practice","attend"]

solution = Solution()
print(solution.prefixCount(words, pref))