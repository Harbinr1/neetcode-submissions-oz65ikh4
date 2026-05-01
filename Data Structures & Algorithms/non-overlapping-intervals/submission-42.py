class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        curr = intervals[0][1]
        res = 0


        for i in range(1,len(intervals)):
            if curr <= intervals[i][0]:
                curr = intervals[i][1]
            else:
                res += 1
                curr = min(curr,intervals[i][1])
        return res