class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = defaultdict(list)
        components = 0
        visited = set()
        for (a,b) in edges:
            preMap[a].append(b)
            preMap[b].append(a)
        

        def dfs(node):
            visited.add(node)

            for neighbor in preMap[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components