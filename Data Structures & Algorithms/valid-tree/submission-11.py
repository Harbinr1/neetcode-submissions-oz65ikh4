class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        map = defaultdict(list)
        edge_count = 0 
        if len(edges) != n-1 :
            return False
        

        for (a,b) in edges:
            map[a].append(b)
            map[b].append(a)
            edge_count +=1
        

        q = deque([0])

        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in map[node]:
                    if neighbor not in visited:
                        q.append(neighbor)

        return len(visited) == n 
