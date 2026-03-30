class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        path = []
        res = []


        mapping = {'2':'abc','3':'def','4':'hgi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}



        def dfs(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            letters = mapping[digits[i]]

            for letter in letters:
                path.append(letter)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return res