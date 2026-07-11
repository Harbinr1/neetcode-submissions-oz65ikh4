class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        substack = []
        result = []
        candidates.sort()
        def dfs(start_index,target):
            if target == 0:
                result.append(substack[:])
                return
            if target < 0:
                return
            
            for i in range(start_index,len(candidates)):
                 
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    return
                substack.append(candidates[i])
                dfs(i+1,target-candidates[i])
                substack.pop()
        
        dfs(0,target)
        return result