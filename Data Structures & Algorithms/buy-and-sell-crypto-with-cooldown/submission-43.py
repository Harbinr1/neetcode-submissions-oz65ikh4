class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        def dfs(i,holding):
            if i >= n:
                return 0
            if dp[i][holding] != -1:
                return dp[i][holding]
            

            if holding:
                sell = prices[i] + dfs(i+2,0)
                hold = dfs(i+1,1)
                dp[i][holding] = max(sell,hold)
                return dp[i][holding]
            else:
                buy = -prices[i] + dfs(i+1,1)
                skip = dfs(i+1,0)
                dp[i][holding] = max(buy,skip)
                return dp[i][holding]

        return dfs(0,0)
        