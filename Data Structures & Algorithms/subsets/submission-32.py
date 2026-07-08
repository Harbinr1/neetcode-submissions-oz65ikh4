class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_subset = []

        def dfs(i):
            if i>=len(nums):
                result.append(current_subset[:])
                return
            
            current_subset.append(nums[i])
            dfs(i+1)
            current_subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result

        