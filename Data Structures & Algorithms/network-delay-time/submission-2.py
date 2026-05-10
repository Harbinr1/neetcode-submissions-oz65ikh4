class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0,k)]
        graph = defaultdict(list)
        visited = set()
        dist = [float('inf')] * (n+1)
        dist[k] = 0


        for u,v,t in times:
            graph[u].append((v,t))
        

        while heap:
            curr_time,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)

            for nei,t in graph[node]:
                new_time = curr_time + t
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap,(new_time,nei))
        
        if any(dist[i] == float('inf') for i in range(1,n+1)):
            return -1
        else:
            return max(dist[1:])

        