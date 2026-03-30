class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(i):
            if i == len(s):
                res.append(path[:])
            
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return res