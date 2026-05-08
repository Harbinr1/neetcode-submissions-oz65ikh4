class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        start = 0
        end = 0
        lastIndex = defaultdict(int)
        for i,c in enumerate(s):
            lastIndex[c] = i
        
        for i,c in enumerate(s):
            end = max(end,lastIndex[s[i]])
            if i == end:
                res.append(end-start + 1)
                start = end + 1
        return res