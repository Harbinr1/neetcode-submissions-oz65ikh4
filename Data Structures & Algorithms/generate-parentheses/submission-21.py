class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(path,open_count,close_count):
            if open_count == n and close_count == n:
                res.append(path)
            

            if open_count < n:
                dfs(path + "(",open_count + 1,close_count)
            
            if open_count > close_count:
                dfs(path + ")",open_count,close_count + 1)
        
        dfs("",0,0)
        return res