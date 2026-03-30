class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = defaultdict(list)
        visited = set()

        for (a,b) in edges:
            map[a].append(b)
            map[b].append(a)
        
        q = deque()
        component = 0
        for node in range(n):
            if node not in visited:
                component +=1 
                q.append(node)
                visited.add(node)
                while q:
                    new_node = q.popleft()
                    for neighbor in map[new_node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
        return component
