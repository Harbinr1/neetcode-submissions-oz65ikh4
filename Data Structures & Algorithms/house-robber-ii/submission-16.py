class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        
        def linear_rob(houses):
            m = len(houses)
            if m == 0:
                return 0
            if m == 1:
                return houses[0]
            
            dp = [0] * m
            dp[0] = houses[0]
            dp[1] = max(houses[0],houses[1])

            for i in range(2,m):
                dp[i] = max(dp[i-1],dp[i-2] + houses[i])
            
            return dp[-1]

        case1 = linear_rob(nums[:-1])
        case2 = linear_rob(nums[1:])
        return max(case1,case2)