class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        i = 0
        heap = []
        res = [-1] * len(queries)
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key = lambda x:x[1])
        

        for index,val in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= val:
                heapq.heappush(heap,(intervals[i][1] - intervals[i][0] + 1,intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < val:
                heapq.heappop(heap)
            
            if not heap:
                continue
            else:
                res[index] = heap[0][0]
        return res