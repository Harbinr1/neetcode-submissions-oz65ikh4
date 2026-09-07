class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(","}":"{","]":"["}


        stack = []


        for char in s:
            if char  in "([{":
                stack.append(char)
            
            else:
                if not stack:
                    return False
                
                if stack.pop() != map[char]:
                    return False
        
        return not stack