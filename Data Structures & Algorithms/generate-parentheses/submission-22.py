class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current = ""
        result = []
        def dfs(current,open,close):
            if open == n and close == open:
                result.append(current)
                return
            
            if open < n:
                dfs(current + "(", open + 1,close)
            
            if close < open:
                dfs(current + ")",open,close +  1)
        
        dfs("",0,0)
        return result


        