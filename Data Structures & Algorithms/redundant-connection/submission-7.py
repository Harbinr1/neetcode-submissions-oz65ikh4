class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}


        for u,v in edges:
            parent[u] = u
            parent[v] = v
        

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        

        def union(u,v):
            parent[find(u)] = find(v)
        

        for u,v in edges:
            if find(u) == find(v):
                return [u,v]
            union(u,v)