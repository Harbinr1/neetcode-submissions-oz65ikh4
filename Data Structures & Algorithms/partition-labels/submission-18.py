class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastIndex = defaultdict(int)
        for i,c in enumerate(s):
            lastIndex[c] = i
        
        size,end = 0,0
        res = []
        for i in range(len(s)):
            end = max(end,lastIndex[s[i]])
            if i == end:
                res.append(end - size + 1)
                size = end + 1
        return res
        