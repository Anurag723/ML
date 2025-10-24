class PracSud:
    def solveSudoku(self, board):
        self.solve(board)

    # Recursive backtracking solver
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):  # '1' to '9'
                        if self.possible(board, i, j, num):
                            board[i][j] = num

                            if self.solve(board):
                                return True

                            board[i][j] = '.'  # Backtrack
                    return False  # No valid number fits here
        return True  # Solved

    # Check if num can be placed in (row, col)
    def possible(self, board, row, col, num):
        # Check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check 3x3 subgrid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    # Utility to print the Sudoku board
    @staticmethod
    def print_board(board):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("------+-------+------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(board[i][j], end=" ")
            print()
        print()


if __name__ == "__main__":
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]

    print("Original Sudoku:")
    PracSud.print_board(board)

    solver = PracSud()
    solver.solveSudoku(board)

    print("Solved Sudoku:")
    PracSud.print_board(board)
