class Solution:
    def checkValidString(self, s: str) -> bool:
        high = 0
        low = 0

        for c in s:
            if c == "(":
                high += 1
                low += 1
            elif c == ")":
                high -= 1
                low -= 1
            
            else:
                high += 1
                low -= 1
            
            if high < 0:
                return False
            if low < 0:
                low = 0
        
        return low == 0
        