class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]



        def dfs(r,c):
            if (r,c) in visited:
                return
            
            visited.add((r,c))

            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[r][c] == 'O':
                    dfs(nr,nc)

        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][COLS-1] == 'O':
                dfs(r,COLS-1)

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1,c)
         






        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'