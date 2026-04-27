class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        current = intervals[0][1]

        for start,end in intervals[1:]:
            if start >= current:
                current = end
            else:
                res += 1
                current = min(end,current)
        
        return res
        
        