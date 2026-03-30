class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def dfs(start,target):
            if target  == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            
            for j in range(start,len(candidates)):
                if candidates[j] > target:
                    break
                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                
                path.append(candidates[j])
                dfs(j+1,target - candidates[j])
                path.pop()
        dfs(0,target)
        return res


                
        