class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1,len(s)+1):
            for word in wordDict:
                lenWord = len(word)
                if i >= lenWord and dp[i-lenWord] and s[i-lenWord:i] == word:
                    dp[i] = True
        

        return dp[len(s)]
        