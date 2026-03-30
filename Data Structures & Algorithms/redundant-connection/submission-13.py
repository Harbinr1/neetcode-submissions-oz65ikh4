class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}


        for (a,b) in edges:
            parent[a] = a
            parent[b] = b
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a,b):
            parent[find(a)] = find(b)


        for a,b in edges:
            if find(a) == find(b):
                return [a,b]
            union(a,b)
        

