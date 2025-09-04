class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = low + (high - low) // 2
            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


# Test the function with sample inputs
if __name__ == "__main__":
    solution = Solution()

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

    print("Searching for 3:", solution.searchMatrix(matrix, 3))     # True
    print("Searching for 13:", solution.searchMatrix(matrix, 13))   # False
