class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = defaultdict(list)
        in_progress = set()
        finished = set()

        for [a,b] in prerequisites:
            map[a].append(b)
        

        def dfs(course):
            if course in finished:
                return True
            
            if course in in_progress:
                return False
            
            in_progress.add(course)

            for prereq in map[course]:
                if not dfs(prereq):
                    return False
            in_progress.remove(course)
            finished.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True