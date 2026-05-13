class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        size = 0 
        lastIndex = defaultdict(int)
        farthest = 0
        for i,v in enumerate(s):
            lastIndex[v] = i
        

        for i in range(len(s)):
            size += 1
            farthest = max(farthest,lastIndex[s[i]])
            if i == farthest:
                res.append(size)
                size = 0
        
        return res
                