class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        res = []
        end = 0
        start = 0
        for i,ch in enumerate(s):
            last[ch] = i
        
        for i in range(len(s)):

            end = max(end,last[s[i]])
            if i == end:
                res.append(end - start+ 1 )
                start = end + 1
        return res