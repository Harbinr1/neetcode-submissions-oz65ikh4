class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        map = defaultdict(list)
 
        if len(edges) != n-1 :
            return False
        

        for (a,b) in edges:
            map[a].append(b)
            map[b].append(a)
        

        q = deque([0])

        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in map[node]:
                    if neighbor not in visited:
                        q.append(neighbor)

        return len(visited) == n 
