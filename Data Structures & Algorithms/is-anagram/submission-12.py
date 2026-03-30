class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s2 = sorted(t)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s1[i] != s2[i]:
                return False
        return True