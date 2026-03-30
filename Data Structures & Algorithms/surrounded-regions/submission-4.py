class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border_set = set()
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        q = deque()
        for r in range(ROWS):
            border_set.add((r,0))
        
        for c in range(COLS):
            border_set.add((0,c))
        

        for r in range(ROWS):
            border_set.add((r,COLS-1))
        for c in range(COLS):
            border_set.add((ROWS-1,c))
        
        for (r,c) in border_set:
            if board[r][c] == 'O':
                q.append((r,c))
                visited.add((r,c))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr< ROWS and 0 <= nc < COLS:
                    if board[nr][nc] == 'O' and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'
        
        

        
        