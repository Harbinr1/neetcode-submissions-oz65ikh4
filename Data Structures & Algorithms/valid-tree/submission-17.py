class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        premap = defaultdict(list)

        if len(edges) != n-1:
            return False
        
        for (a,b) in edges:
            premap[a].append(b)
            premap[b].append(a)
        

        def dfs(node,parent):
            visited.add(node)

            for neighbor in premap[node]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return True
                
                if dfs(neighbor,node):
                    return True
            
            return False

        if dfs(0,-1):
            return False
        
        return len(visited) == n