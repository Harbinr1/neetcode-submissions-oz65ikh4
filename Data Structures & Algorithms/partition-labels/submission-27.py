class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = []
        lastIndex = defaultdict(int)

        for i,v in enumerate(s):
            lastIndex[v] = i
        
        end = 0
        farthest = 0
        start = 0
        for i,c in enumerate(s):
            end = max(end,lastIndex[s[i]])
            if i == end:
                size.append(end - start + 1)
                start = end + 1
        return size

        