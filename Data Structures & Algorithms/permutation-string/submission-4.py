from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        l = 0

        for i in s1:
            freq1[i] += 1
    

        for r in range(len(s2)):
            freq2[s2[r]] += 1
            if r - l + 1 == len(s1):
                if freq1 == freq2:
                    return True
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1
        return False
        