class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        total_max = 0
        directions = ([1,0],[-1,0],[0,1],[0,-1])
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            current_max = 0
            for dr,dc in directions:
                nr,nc = dr+i,dc + j
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[i][j]:
                    current_max = max(dfs(nr,nc),current_max)
            
            dp[i][j] = current_max + 1
            return dp[i][j]
        

        for i in range(ROWS):
            for j in range(COLS):
                current_max = dfs(i,j)
                total_max = max(current_max,total_max)
        return total_max
        