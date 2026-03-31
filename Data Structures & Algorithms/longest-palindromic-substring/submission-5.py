class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 1
        start = 0

        n = len(s)
        dp = [[False] * (n) for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if (j - i + 1) <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True

                    if dp[i][j] and (j-i+1) > maxLen:
                        maxLen = j - i + 1
                        start = i
        
        return s[start:start+maxLen]
