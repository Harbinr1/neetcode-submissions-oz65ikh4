class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        'n = 2 ->  ()() (())'
        'string = "" -> ( -> ( or ). (( or ().  (( ) or () (. n = 2 (( )) or () ()   '
        result = []
        def dfs(string,open,close):
            if open == n and close == open:
                result.append(string)
                return 
            
            if open < n:
                dfs(string + "(",open + 1,close)
            if close < open:
                dfs(string+")",open,close + 1)
            
        dfs("",0,0)
        return result