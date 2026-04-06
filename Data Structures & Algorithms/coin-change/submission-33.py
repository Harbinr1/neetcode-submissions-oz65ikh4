class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins = different denominations, int amount -> target amount
        #Return min number of coins to sum up to target.

        #dp -> telling how much denominations we need to form value at i. this should be minimum of i itself or minimum of index - coin value

        n = amount+1
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1,n):
            for c in coins:
                if c <= i:
                    dp [i] = min(dp[i],dp[i-c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1 

        