class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        exploring = set()


        mapEdges = defaultdict(list)

        for a,b in prerequisites:
            mapEdges[a].append(b)
        

        
        def dfs(node):
            if node in visited:
                return True
            if node in exploring:
                return False
            exploring.add(node)

            for nei in mapEdges[node]:
                if not dfs(nei):
                    return False
            exploring.remove(node)
            visited.add(node)
            result.append(node)
            return True
        result = []
        for n in range(numCourses):
            if not dfs(n):
                return []
        return result
        
        