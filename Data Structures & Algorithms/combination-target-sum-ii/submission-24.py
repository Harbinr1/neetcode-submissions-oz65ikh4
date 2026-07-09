class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        substack = []
        result = []
        flag = [False] * len(candidates)
        candidates.sort()
        def dfs(i,target):
            if target == 0:
                result.append(substack[:])
                return
            if target < 0:
                return
            if i >= len(candidates):
                return
            
            if i > 0 and candidates[i] == candidates[i-1] and not flag[i-1]:
                dfs(i+1,target)
                return
            
            flag[i] = True
            substack.append(candidates[i])
            dfs(i+1,target-candidates[i])
            substack.pop()
            flag[i] = False
            dfs(i+1,target)
        
        dfs(0,target)
        return result