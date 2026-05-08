class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        res = []
        size = 0
        end = 0

        for i,c in enumerate(s):
            lastIndex[c] = i
        

        for i,c in enumerate(s):
            end = max(end,lastIndex[c])
            size +=1
            if i == end:
                res.append(size)
                size = 0
        return res

        