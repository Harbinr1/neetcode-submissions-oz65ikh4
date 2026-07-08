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
                    seen.add(n)
                    path.append(n)
                    dfs(path)
                    path.pop()
                    seen.remove(n)
            
        dfs([])
        return result