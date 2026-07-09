class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        substack = []
        result = []
        visited = set()

        def dfs(substack):
            if len(substack) == len(nums):
                result.append(substack[:])
                return
            
            for n in nums:
                if n not in visited:
                    visited.add(n)
                    substack.append(n)
                    dfs(substack)
                    substack.pop()
                    visited.remove(n)
        
        dfs([])
        return result

        
        