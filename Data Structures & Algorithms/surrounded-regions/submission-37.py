class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        for r in range(ROWS):
            if board[r][0] == 'O':
                q.append((r,0))
            if board[r][COLS-1] == 'O':
                q.append((r,COLS-1))
        
        for c in range(COLS):
            if board[0][c] == 'O':
                q.append((0,c))
            if board[ROWS-1][c] == 'O':
                q.append((ROWS-1,c))


        while q:
            r,c = q.popleft()
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if board[nr][nc] == 'O' and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
        


        



        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'