class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_set = set()
        col_set = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)


        for r in row_set:
            for c in range(COLS):
                matrix[r][c] = 0


        for c in col_set:
            for r in range(ROWS):
                matrix[r][c] = 0
                 