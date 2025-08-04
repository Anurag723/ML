class Solution:
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Step 1: Check if first row or first column has zero
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        # Step 2: Use first row and column as markers for zero rows/columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 3: Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 4: Zero out first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Step 5: Zero out first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("Original matrix:")
    for row in matrix:
        print(row)

    sol = Solution()
    sol.setZeroes(matrix)

    print("\nMatrix after setZeroes:")
    for row in matrix:
        print(row)
