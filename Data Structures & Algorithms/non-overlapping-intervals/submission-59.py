class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i][0] < prevEnd[1]:
                res += 1
                prevEnd[1] = min(intervals[i][1],prevEnd[1])
            else:
                prevEnd = intervals[i]
        return res
        