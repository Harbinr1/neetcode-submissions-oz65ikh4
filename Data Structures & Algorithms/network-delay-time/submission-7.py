class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0,k)]
        graph = defaultdict(list)
        visited = set()
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        t = 0

        for u,v,w in times:
            graph[u].append((v,w))
        

        while heap:
            curr_time,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t,curr_time)
            for nei,time in graph[node]:
                new_time = curr_time + time
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap,(new_time,nei))
        
        return t if len(visited) == n else -1