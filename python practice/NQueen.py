class NQueen:
    def solveNQueens(self, n):
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(board, res, 0, n)
        return res

    def solve(self, board, res, srow, n):
        if srow == n:
            temp = [''.join(row) for row in board]
            res.append(temp)
            return

        for i in range(n):
            if self.isSafe(board, srow, i, n):
                board[srow][i] = 'Q'
                self.solve(board, res, srow + 1, n)
                board[srow][i] = '.'  # backtrack

    def isSafe(self, board, row, col, n):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

# Runner code
if __name__ == "__main__":
    n = 4  # You can change this value
    solver = NQueen()
    solutions = solver.solveNQueens(n)

    print(f"Total Solutions: {len(solutions)}")
    for solution in solutions:
        for row in solution:
            print(row)
        print()  # Blank line between solutions
