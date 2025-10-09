def generate_parenthesis(n):
    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            result.append(curr)
            return
        if open_count < n:
            backtrack(curr + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr + ')', open_count, close_count + 1)

    result = []
    backtrack("", 0, 0)
    return result

# Main block
if __name__ == "__main__":
    n = int(input("Enter number of pairs of parentheses (n): "))
    if n < 0:
        print("Number of pairs must be non-negative.")
    else:
        combinations = generate_parenthesis(n)
        print("Generated parentheses combinations:")
        for combo in combinations:
            print(combo)
