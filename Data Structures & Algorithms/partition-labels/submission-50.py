class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        res = []
        farthest = 0

        lastIndex = defaultdict(int)

        for i,c in enumerate(s):
            lastIndex[c] = i
        
        for i in range(len(s)):
            size += 1
            farthest = max(farthest,lastIndex[s[i]])
            if i == farthest:
                res.append(size)
                size = 0
        return res
        