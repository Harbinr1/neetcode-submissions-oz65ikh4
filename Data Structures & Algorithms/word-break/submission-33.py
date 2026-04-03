class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True


        for i in range(len(s)+1):
            for word in wordDict:
                wordLen = len(word)
                if i >= wordLen and dp[i-wordLen] and s[i-wordLen:i] == word:
                    dp[i] = True
        
        return dp[len(s)]
        
        
        