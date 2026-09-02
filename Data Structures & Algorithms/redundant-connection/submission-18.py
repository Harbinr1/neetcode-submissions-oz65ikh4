class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        parent = [i for i in range(N+1)]

        def find(n):
            if parent[n] == n:
                return n
            
            parent[n] = find(parent[n])
            return parent[n]
        

        def union(A,B):
            rootA = find(A)
            rootB = find(B)

            if rootA == rootB:
                return False
            
            if rootA != rootB:
                parent[rootA] = rootB
            return True
        

        for u,v in edges:
            if not union(u,v):
                return [u,v]
            

            
        