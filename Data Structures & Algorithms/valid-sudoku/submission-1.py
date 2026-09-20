from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Sudoku board:
        #          c=0  c=1  c=2  c=3  c=4  c=5  c=6  c=7  c=8
        #
        # r=0       5    3    .    .    7    .    .    .    .
        # r=1       6    .    .    1    9    5    .    .    .
        # r=2       .    9    8    .    .    .    .    6    .
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue

                # Check if number already exists in:
                # 1. Same row
                # 2. Same column
                # 3. Same 3x3 square
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sqs[(r // 3, c // 3)]):
                    return False
                # Number is valid, so remember it
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqs[(r // 3, c // 3)].add(board[r][c])

        return True