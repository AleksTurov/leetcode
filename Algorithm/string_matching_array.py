class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        result = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and word1 in word2:
                    result.append(word1)
                    break
        return result
    
solution = Solution()
words1 = ["mass","as","hero","superhero"]
print(solution.stringMatching(words1))

words2 = ["leetcode","et","code"]
print(solution.stringMatching(words2))

words3 = ["blue","green","bu"]
print(solution.stringMatching(words3))