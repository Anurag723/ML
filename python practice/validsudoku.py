class Solution:
    def isValidSudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                boxidx = (r // 3) * 3 + (c // 3)

                if val in row[r] or val in col[c] or val in box[boxidx]:
                    return False

                row[r].add(val)
                col[c].add(val)
                box[boxidx].add(val)

        return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
print(sol.isValidSudoku(board))  # Output: True
