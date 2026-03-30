class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS = len(board)
        COLS = len(board[0])
        border_set = set()


        for r in range(ROWS):
            border_set.add((r,0))
        for c in range(COLS):
            border_set.add((0,c))

        for r in range(ROWS):
            border_set.add((r,COLS-1))
        for c in range(COLS):
            border_set.add((ROWS-1,c))
        
        q = deque()
        for (r,c) in border_set:
            if board[r][c] == 'O':
                border_set.add((r,c))
                q.append((r,c))
        
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if board[nr][nc] == 'O' and (nr,nc) not in border_set:
                        border_set.add((nr,nc))
                        q.append((nr,nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in border_set:
                    board[r][c] = 'X'
