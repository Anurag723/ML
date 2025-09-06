def findPeakGrid(mat):
    rows = len(mat)
    cols = len(mat[0])
    
    left = 0
    right = cols - 1

    while left <= right:
        mid = (left + right) // 2

        # Find the row index with the max value in the middle column
        max_row = 0
        for i in range(rows):
            if mat[i][mid] > mat[max_row][mid]:
                max_row = i

        left_is_bigger = mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]
        right_is_bigger = mid < cols - 1 and mat[max_row][mid + 1] > mat[max_row][mid]

        if not left_is_bigger and not right_is_bigger:
            return [max_row, mid]
        elif left_is_bigger:
            right = mid - 1
        else:
            left = mid + 1

    return None  # Should not reach here if input is valid


# 🧪 Main function to test the code
if __name__ == "__main__":
    mat = [
        [10, 8, 10, 10],
        [14, 13, 12, 11],
        [15, 9, 11, 21],
        [16, 17, 19, 20]
    ]

    result = findPeakGrid(mat)
    if result:
        i, j = result
        print(f"Peak found at: [{i}, {j}] with value: {mat[i][j]}")
    else:
        print("No peak found.")
