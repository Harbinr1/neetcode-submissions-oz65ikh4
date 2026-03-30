class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(path,open,close):
            if open == n and close == n:
                res.append("".join(path))
            
            if open < n:
                path.append("(")
                dfs(path,open +1,close)
                path.pop()
            
            if open > close:
                path.append(")")
                dfs(path,open,close+1)
                path.pop()
            
        dfs([],0,0)
        return res
        