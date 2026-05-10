class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = [(0,k)]
        dist = [float('inf')] * ( n +1)
        dist[k] = 0
        edges = defaultdict(list)
        t = 0
        visited = set()


        for u,v,w in times:
            edges[u].append((v,w))
        

        while minHeap:
            curr_time,node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t,curr_time)

            for nei,time in edges[node]:
                new_time = curr_time + time
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(minHeap,(new_time,nei))
        return t if len(visited) == n else - 1