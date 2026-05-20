from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(curr_sub,t):
            sub_counts = Counter(curr_sub)
            t_counts = Counter(t)
            for char in t_counts:
                if sub_counts[char] < t_counts[char]:
                    return False
            return True
        left = 0
        right = 0
        min_valid = float('inf')
        result = ""

        while right < len(s):
            curr_validsub = s[left:right+1]
            if is_valid(curr_validsub,t):
                if len(curr_validsub) < min_valid:
                    min_valid = len(curr_validsub)
                    result = curr_validsub
            
                left += 1
            else:
                right += 1
        return result

        