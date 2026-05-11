class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        res = []
        stack = ["JFK"]

        for s,t in tickets:
            graph[s].append(t)
        
        for flight in graph:
            graph[flight].sort(reverse = True)
        

        while stack:
            current = stack[-1]
            if graph[current]:
                next_flight = graph[current].pop()
                stack.append(next_flight)
            else:
                res.append(stack.pop())
        return res[::-1]
        