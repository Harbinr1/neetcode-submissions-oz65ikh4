class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        
        heap = []
        heapq.heappush(heap,(dist[k],k))
        connections = defaultdict(list)

        for (u,v,t) in (times):
            connections[u].append((t,v))
        

        while heap:
            curr_dist,node = heapq.heappop(heap)

            for time,nei in connections[node]:
                curr_time = time + curr_dist
                if curr_time < dist[nei]:
                    dist[nei] = curr_time
                    heapq.heappush(heap,(curr_time,nei))
        
        maxT = 0
        for t,n in enumerate(dist):

            if t > 0 and n > maxT:
                maxT = n
            
            if n == float('inf') and t > 0:
                return -1
        
        return maxT

