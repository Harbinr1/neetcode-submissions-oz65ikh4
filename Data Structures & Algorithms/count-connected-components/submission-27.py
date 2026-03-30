class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = defaultdict(list)
        components = 0
        visited = set()
        q = deque()
        for (a,b) in edges:
            preMap[a].append(b)
            preMap[b].append(a)
        

        def bfs(node):
            q = deque([node])
            visited.add(node)

            while q:
                curr = q.popleft()
                for neighbor in preMap[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        for node in range(n):
            if node not in visited:
                components += 1
                bfs(node)
        return components