class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for (x,y) in points:
            distance = (x**2+y**2)
            heapq.heappush(minHeap,(distance,[x,y]))
        

        res = []

        while len(res)<k:
            dist,point = heapq.heappop(minHeap)
            res.append(point)
        
        return res
        