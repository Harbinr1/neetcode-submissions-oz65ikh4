class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        countS = defaultdict(int)
        res_len = float('inf')
        have = 0
        res = ""
        l = 0
        if len(s) < len(t):
            return ""
        for r in range(len(t)):
            countT[t[r]] += 1
        
        need = len(countT)

        for r in range(len(s)):
            countS[s[r]] += 1

            if countS[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if (r-l + 1) < res_len:
                    res_len = r-l+1
                    res = s[l:r+1]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res
        