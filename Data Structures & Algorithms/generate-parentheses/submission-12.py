class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(path,open,close):
            if open == n and close == n:
                res.append(path)
                
            
            if open < n:
                dfs(path + "(",open+1,close)
            if open > close:
                dfs(path + ")",open,close + 1)
        
        dfs("",0,0)
        return res