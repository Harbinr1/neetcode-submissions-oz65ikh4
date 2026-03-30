class Solution:
    def isValid(self, s: str) -> bool:
        countPar = { ")":"(","]":"[","}":"{" }
        res = []
        if len(s) <= 1:
            return False
        
        for par in s:
            if par in "([{":
                res.append(par)
            elif par in ")]}":
                if not res:
                    return False
                if res.pop() != countPar[par]:
                    return False

        return not bool(res)

        