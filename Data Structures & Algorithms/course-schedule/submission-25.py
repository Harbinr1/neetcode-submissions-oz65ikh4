class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = [[] for _ in range(numCourses)]
        current_path = set()


        for (a,b) in prerequisites:
            graph[b].append(a)


        def dfs(course):
            if course in visited:
                return True
            
            if course in current_path:
                return False
            current_path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            current_path.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
