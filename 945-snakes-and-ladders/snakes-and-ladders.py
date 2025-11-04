from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        # Helper: Convert a square number to (row, col)
        def get_coordinates(num):
            r = (num - 1) // n
            c = (num - 1) % n
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square, moves)

        while queue:
            num, moves = queue.popleft()
            if num == n * n:
                return moves
            for step in range(1, 7):
                next_num = num + step
                if next_num > n * n:
                    continue
                r, c = get_coordinates(next_num)
                if board[r][c] != -1:
                    next_num = board[r][c]
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, moves + 1))
        return -1
