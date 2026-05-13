class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        processing = set()

        def dfs(i):
            graph = defaultdict(list)
            for s,t in prerequisites:
                graph[s].append(t)
            if i in processing:
                return False
            
            if i in visited:
                return True
            

            
            processing.add(i)

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            processing.remove(i)
            visited.add(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
            

        