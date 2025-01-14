class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sumn=0
        for i in range(len(s)-1):
            sumn += abs(ord(s[i]) - ord(s[i + 1]))

        return  sumn
        