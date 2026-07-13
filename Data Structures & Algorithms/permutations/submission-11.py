class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        subset = []
        result = []

        def dfs(subset):
            if len(subset) >= len(nums):
                result.append(subset[:])
                return
            
            for n in nums:
                if n not in seen:
                    seen.add(n)
                    subset.append(n)
                    dfs(subset)
                    subset.pop()
                    seen.remove(n)
        
        dfs([])
        return result
        