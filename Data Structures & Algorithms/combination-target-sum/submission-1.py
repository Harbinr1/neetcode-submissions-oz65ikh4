class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i,target):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return
            
            if i >= len(nums):
                return
            
            path.append(nums[i])
            dfs(i,target - nums[i])

            path.pop()
            dfs(i+1,target)
        
        dfs(0,target)
        return res
        