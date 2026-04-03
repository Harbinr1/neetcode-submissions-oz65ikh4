class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)+ 1):
            if not dp[i]:
                continue

            for word in wordDict:
                lenW = len(word)
                if i + lenW <= len(s) and s[i:i + lenW] == word:
                    dp[i+lenW] = True
        
        return dp[len(s)]
        

        
        
        