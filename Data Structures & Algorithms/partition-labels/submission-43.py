class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)

        for i,c in enumerate(s):
            lastIndex[c] = i
        
        size = 0
        farthest = 0
        res = []
        
        for i in range(len(s)):
            size += 1
            farthest = max(farthest,lastIndex[s[i]])
            if i == farthest:
                res.append(size)
                size = 0
        return res
        