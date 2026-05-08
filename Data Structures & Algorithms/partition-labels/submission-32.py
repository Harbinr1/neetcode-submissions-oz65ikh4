class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        end = 0
        start = 0
        lastInd =defaultdict(int)

        for i,c in enumerate(s):
            lastInd[c] = i
        
        for i in range(len(s)):
            end = max(end,lastInd[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res