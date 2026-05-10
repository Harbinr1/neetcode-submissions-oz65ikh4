class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = [(0,k)]
        visited = set()
        edges = defaultdict(list)
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        t = 0


        for u,v,w in times:
            edges[u].append((v,w))


        while minHeap:
            curr_time,node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t,curr_time)

            for node,time in edges[node]:
                new_time = curr_time + time
                if new_time < dist[node]:
                    dist[node] = new_time
                    heapq.heappush(minHeap,(new_time,node))
        return t if len(visited) == n else - 1