class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        for u,v in edges:
            parent[u] = u
            parent[v] = v
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        

        def union(x,y):
            parent[find(x)] = find(y)
        
        for u,v in edges:
            if find(u) == find(v):
                return [u,v]
            union(u,v)
        