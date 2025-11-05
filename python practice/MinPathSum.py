class MinPathSum:
    @staticmethod
    def get_min_path_sum(grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        # Initialize top-left cell
        dp[0][0] = grid[0][0]

        # Fill first row
        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Fill first column
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Fill the rest of the table
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp


if __name__ == "__main__":
    # Example input grid (you can change this)
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    # Compute the minimum path sum table
    min_path = MinPathSum.get_min_path_sum(grid)

    # Print the result
    print("Minimum Path Sum Table:")
    for row in min_path:
        print(" ".join(map(str, row)))
