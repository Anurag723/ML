def generate(numRows):
    res = []

    for i in range(numRows):
        row = [1]  # First element is always 1

        for j in range(1, i):
            prelft = res[i - 1][j - 1]
            preright = res[i - 1][j]
            row.append(prelft + preright)

        if i > 0:
            row.append(1)  # Last element is also 1 (if i > 0)

        res.append(row)

    return res

triangle = generate(5)
for row in triangle:
    print(row)
