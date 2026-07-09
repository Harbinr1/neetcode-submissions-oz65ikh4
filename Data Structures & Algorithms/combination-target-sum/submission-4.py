class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        substack = []
        result = []

        def dfs(i,target):
            if target == 0:
                result.append(substack[:])
                return
            
            if target < 0:
                return
            
            if i >= len(nums):
                return
            
            substack.append(nums[i])
            dfs(i,target-nums[i])
            substack.pop()
            dfs(i+1,target)
        
        dfs(0,target)
        return result
        