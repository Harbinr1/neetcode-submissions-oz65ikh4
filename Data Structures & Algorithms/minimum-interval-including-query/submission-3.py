class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key = lambda x:x[1])
        res = [-1] * len(queries)
        heap = []
        i = 0


        for index,val in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= val:
                heapq.heappush(heap,(intervals[i][1] - intervals[i][0] + 1,intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < val:
                heapq.heappop(heap)
            
            if not heap:
                res[index] = -1
            else:
                res[index] = heap[0][0]

        return res 


        