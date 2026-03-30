class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = [[] for _ in range(n)]
        

        if len(edges) != n-1:
            return False
        

        for (a,b) in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(node,parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return True

                if dfs(neighbor,node):
                    return True

        if dfs(0,-1):
            return False

        return len(visited) == n        