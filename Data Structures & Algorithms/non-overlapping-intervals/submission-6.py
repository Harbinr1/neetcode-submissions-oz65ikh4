class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        res = 0
        current = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= current[1]:
                current = intervals[i]
            else:
                res += 1
                 
                


        return res 
        