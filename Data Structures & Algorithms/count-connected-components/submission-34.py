class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visited = set()
        preMap = defaultdict(list)
        for (a,b) in edges:
            preMap[a].append(b)
            preMap[b].append(a)



        def bfs(node):
            q = deque([node])

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