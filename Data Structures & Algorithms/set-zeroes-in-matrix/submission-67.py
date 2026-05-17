class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = False
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_zero = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        
        