class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        overall_max = 0

        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        directions = ([1,0],[-1,0],[0,1],[0,-1])
        
        def dfs(i,j):
            current_path = 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            for dr,dc in directions:
                ni,nj = dr+i,dc+j
                if 0 <= ni < ROWS and 0 <= nj < COLS and matrix[ni][nj] > matrix[i][j]:
                    current_path = max(dfs(ni,nj),current_path)
            
            dp[i][j] = 1 + current_path
            return dp[i][j]

        for i in range(ROWS):
            for j in range(COLS):
                current_path = dfs(i,j)
                overall_max = max(current_path,overall_max)
        return overall_max


        