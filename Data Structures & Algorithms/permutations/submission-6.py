class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        seen = set()
        

        def dfs(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for n in nums:
                if n not in seen:
                    path.append(n)
                    seen.add(n)
                    dfs(path)
                    path.pop()
                    seen.remove(n)
        dfs([])
        
        return result
            