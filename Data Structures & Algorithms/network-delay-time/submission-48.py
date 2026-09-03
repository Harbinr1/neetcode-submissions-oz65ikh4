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
        
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1

