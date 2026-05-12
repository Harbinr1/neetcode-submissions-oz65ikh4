class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        minHeap = [(0,k)]
        visited = set()
        t = 0
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        

        while minHeap:
            time,currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            visited.add(currNode)
            t = max(t,time)

            for nei,nei_time in graph[currNode]:
                new_time = nei_time + time
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(minHeap,(new_time,nei))

        return t if len(visited) == n else - 1

        