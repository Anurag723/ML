class WordSearch:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, row, col, index):
        if index == len(word):
            return True

        if (row < 0 or row >= len(board) or
            col < 0 or col >= len(board[0]) or
            board[row][col] != word[index]):
            return False

        temp = board[row][col]
        board[row][col] = '*'  # Mark as visited

        # Explore in all 4 directions
        found = (self.dfs(board, word, row + 1, col, index + 1) or
                 self.dfs(board, word, row - 1, col, index + 1) or
                 self.dfs(board, word, row, col + 1, index + 1) or
                 self.dfs(board, word, row, col - 1, index + 1))

        board[row][col] = temp  # Backtrack
        return found


if __name__ == "__main__":
    ws = WordSearch()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"

    print(f'Word "{word1}" exists:', ws.exist([row[:] for row in board], word1))  # True
    print(f'Word "{word2}" exists:', ws.exist([row[:] for row in board], word2))  # True
    print(f'Word "{word3}" exists:', ws.exist([row[:] for row in board], word3))  # False
