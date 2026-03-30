class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for n in nums:
                if n not in visited:
                    path.append(n)
                    visited.add(n)
                    dfs(path)
                    path.pop()
                    visited.remove(n)
        dfs([])
        return res
        
        