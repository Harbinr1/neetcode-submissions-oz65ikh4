from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countS,countT = defaultdict(int),defaultdict(int)

        for char in s:
            countS[char] += 1
        for char in t :
            countT[char] += 1
        
        for i in countS:
            if countS[i] != countT[i]:
                return False
        return True
