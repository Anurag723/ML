class Searchin2DII:
    def searchMatrix(self, matrix, target):
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False

# Runner code
if __name__ == "__main__":
    solution = Searchin2DII()

    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    target = 5

    result = solution.searchMatrix(matrix, target)
    print(f"Target {target} {'found' if result else 'not found'}.")
