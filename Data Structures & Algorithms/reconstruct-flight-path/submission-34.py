class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        minHeap = []
        stack = [("JFK")]
        graph = defaultdict(list)
        res = []
        for s,t in tickets:
            graph[s].append(t)
        

        for flight in graph:
            heapq.heapify(graph[flight])
        

        while stack:
            curr = stack[-1]
            if graph[curr]:
                next_flight = heapq.heappop(graph[curr])
                stack.append(next_flight)
            else:
                res.append(stack.pop())
        return res[::-1]