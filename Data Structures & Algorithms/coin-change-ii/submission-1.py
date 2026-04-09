class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for j in range(amount + 1)] for i in range(len(coins))]
        
        def dfs(i,rem):
            if rem == 0:
                return 1
            if rem < 0 or i >= len(coins):
                return 0
            
            if dp[i][rem] != -1:
                return dp[i][rem]
            
            take = dfs(i,rem-coins[i])
            skip = dfs(i+1,rem)

            dp[i][rem] = skip + take
            return dp[i][rem]
        
        return dfs(0,amount)
    