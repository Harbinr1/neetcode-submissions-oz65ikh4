class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i,rem):
            if (i,rem) in dp:
                return dp[(i,rem)]
            
            if i == len(nums):
                return 1 if rem == 0 else 0
            
            plus = dfs(i+1,rem + nums[i])
            minus = dfs(i+1,rem - nums[i])
            dp[(i,rem)] = plus + minus
            return dp[(i,rem)]
        
        return dfs(0,target)
        