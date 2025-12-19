class Triangle120:
    @staticmethod
    def minimumTotal(triangle):
        if not triangle:
            return 0

        # Bottom-up DP
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1]
                )

        return triangle[0][0]


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    result = Triangle120.minimumTotal(triangle)
    print("Minimum path sum:", result)  # Expected: 11
