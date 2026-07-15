class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()

        mapCourse = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            mapCourse[b].append(a)

        
        def dfs(course):
            if course in path:
                return False
            
            if course in visited:
                return True
            

            path.add(course)

            for nei in mapCourse[course]:
                if not dfs(nei):
                    return False
            
            path.remove(course)
            visited.add(course)
            return True
        

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True


        