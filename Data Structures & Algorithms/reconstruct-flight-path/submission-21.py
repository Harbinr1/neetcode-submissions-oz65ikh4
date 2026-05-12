class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        stack = []
        stack = [("JFK")]
        graph = defaultdict(list)
        res = []
        minHeap = []
        for s,t in tickets:
            graph[s].append(t)
        
        for flight in graph:
            graph[flight].sort(reverse=True)
        

        while stack:
            curr = stack[-1]
            if graph[curr]:
                next_flight = graph[curr].pop()
                stack.append(next_flight)
            else:
                res.append(stack.pop())
        return res[::-1]

        