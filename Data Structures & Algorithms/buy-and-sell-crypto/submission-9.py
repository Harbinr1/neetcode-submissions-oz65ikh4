class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r =0
        max_profit = 0

        while r < len(prices):
        
            if prices[l] < prices[r]:
                max_profit = max(max_profit,(prices[r] - prices[l]))
                r += 1
            elif prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1

            
        
        return max_profit if max_profit > 0 else 0