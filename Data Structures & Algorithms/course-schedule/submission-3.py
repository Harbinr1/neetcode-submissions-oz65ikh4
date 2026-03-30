class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = defaultdict(list)
        current_path = set()
        finished = set()
        for [a,b] in prerequisites:
            map[a].append(b)
        
        def dfs(course):
            if course in finished:
                return True
            
            if course in current_path:
                return False
            
            current_path.add(course)
            for prereq in map[course]:
                if not dfs(prereq):
                    return False
            current_path.remove(course)
            finished.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            


        