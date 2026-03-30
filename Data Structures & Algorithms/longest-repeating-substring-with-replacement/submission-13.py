from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        r = 0
        max_count = 0
        max_length = 0

        for r in range(len(s)):
            c =s[r]  
            count[c] += 1
            max_count = max(max_count,count[c])

            while r - l + 1 - max_count > k:
                count[s[l]] -= 1
                l += 1
            max_length = max(max_length,r - l + 1)
        return max_length
        
