class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = float('-inf')

        if not prices or len(prices) < 2:
            return 0 
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            maxProfit = max(maxProfit,prices[i]-minPrice)
        
        return maxProfit if maxProfit > 0 else 0 
        