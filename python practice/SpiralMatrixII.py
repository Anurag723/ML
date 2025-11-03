def generate_matrix(n):
    res = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        # left → right
        for i in range(left, right + 1):
            res[top][i] = num
            num += 1
        top += 1

        # top → bottom
        for i in range(top, bottom + 1):
            res[i][right] = num
            num += 1
        right -= 1

        # right → left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1

        # bottom → top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1

    return res


# Example usage:
if __name__ == "__main__":
    n = 4
    matrix = generate_matrix(n)
    print(f"Spiral {n}x{n} Matrix:")
    for row in matrix:
        print(*row)
