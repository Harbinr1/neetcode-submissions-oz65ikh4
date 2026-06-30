class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        minLen = float('inf')
        countT = Counter(t)
        countS = defaultdict(int)
        have = 0
        need = len(countT) 

        start,end = 0,0
        for r in range(len(s)):
            char = s[r]
            countS[char] += 1

            if char in countT and countS[char] == countT[char]:
                have += 1
            
            while have == need:
                if (r-l + 1) < minLen:
                    minLen = r-l +1
                    start,end = l,r
                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return s[start:end+1] if minLen != float('inf') else "" 

