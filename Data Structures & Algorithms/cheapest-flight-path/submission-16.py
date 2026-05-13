class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        visited = set()
        minH = [(0,src,0)]

        graph = defaultdict(list)

        for s,t,p in flights:
            graph[s].append((t,p))
        best = {}
        while minH :
            prc,node,stops = heapq.heappop(minH)
            

            if node == dst:
                return prc
            if stops > k:
                continue

            if (node,stops) in best and best[(node,stops)] <= prc:
                continue
            best[(node,stops)] = prc


            for nei,price in graph[node]:
                heapq.heappush(minH,(prc+price,nei,stops + 1))
        return -1