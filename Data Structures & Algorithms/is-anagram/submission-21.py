from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT,countS = defaultdict(int),defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        

        for char in countS:
            if countS[char] != countT[char]:
                return False
        return True

        