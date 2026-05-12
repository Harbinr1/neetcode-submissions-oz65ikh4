class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        minHeap = []
        visited = set()

        minHeap= [(0,0)]

        while len(visited) < len(points):
            cost,i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            total += cost
            for j in range(len(points)):
                x1,x2 = points[i]
                y1,y2 = points[j]

                dist = abs(x1-y1) + abs(x2-y2)
                heapq.heappush(minHeap,(dist,j))
        return total
        