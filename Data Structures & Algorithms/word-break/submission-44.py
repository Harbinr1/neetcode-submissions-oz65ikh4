class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1,n+1):
            for word in wordDict:
                lenW = len(word)
                if i >= lenW and dp[i-lenW] and s[i-lenW:i] == word:
                        dp[i] = True
        

        return dp[len(s)]