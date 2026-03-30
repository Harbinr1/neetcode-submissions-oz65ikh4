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


        for x,y in edges:
            if find(x) == find(y):
                return [x,y]
            union(x,y)        