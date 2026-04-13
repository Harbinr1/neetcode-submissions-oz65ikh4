class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for j in range(2)] for i in range(len(prices))]

        def dfs(i,holding):
            if i >= len(prices):
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
                hold = dfs(i+1,0)
                dp[i][holding] = max(buy,hold)
                return dp[i][holding]
        
        return dfs(0,0)
        