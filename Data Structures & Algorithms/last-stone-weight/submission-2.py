import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap) >= 2:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap,-(y-x))
        
        if not heap:
            return 0 
        else:
            return -heap[0]

        

        