class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        countS = defaultdict(int)
        res = ""
        min_res = float('inf')
        have = 0
        l = 0
        for r in range(len(t)):
            countT[t[r]] += 1
        need = len(countT)

        for r in range(len(s)):
            countS[s[r]] += 1

            if countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < min_res:
                    min_res = r-l+1
                    res = s[l:r+1]
                
                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return res if min_res != float('inf') else ""