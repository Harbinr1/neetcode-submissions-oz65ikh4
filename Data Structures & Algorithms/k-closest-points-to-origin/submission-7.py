class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x,y = point
            distance = (x**2) + (y**2)

            heapq.heappush(heap,(-(distance),(x,y)))
            if len(heap) > k:
                heapq.heappop(heap)
            
        closest_point = [point for (_,point) in heap]
        
        return closest_point
        