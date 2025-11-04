class Solution:
    def updateBoard(self, board, click):
        rows, cols = len(board), len(board[0])
        r, c = click
        
        # If mine clicked
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        # DFS function
        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < cols) or board[x][y] != 'E':
                return
            
            # Count adjacent mines
            mines = 0
            directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'M':
                    mines += 1
            
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    dfs(x + dx, y + dy)
        
        dfs(r, c)
        return board
