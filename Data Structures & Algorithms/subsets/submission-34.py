class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        substack = []
        result = []

        def dfs(i):
            if i >= len(nums):
                result.append(substack[:])
                return
            
            substack.append(nums[i])
            dfs(i+1)
            substack.pop()
            dfs(i+1)
        
        dfs(0)
        return result
        