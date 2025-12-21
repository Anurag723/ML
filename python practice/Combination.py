class Combination:
    def combine(self, n: int, k: int):
        res = []
        self.backtrack(1, n, k, [], res)
        return res

    def backtrack(self, start: int, n: int, k: int, curr: list, res: list):
        # Base case: when the combination size reaches k
        if len(curr) == k:
            res.append(curr.copy())  # copy current combination
            return

        # Try all possible next numbers
        for i in range(start, n + 1):
            curr.append(i)                 # choose
            self.backtrack(i + 1, n, k, curr, res)  # explore
            curr.pop()                     # un-choose (backtrack)


if __name__ == "__main__":
    c = Combination()

    n = 4
    k = 2

    result = c.combine(n, k)

    # Print the combinations
    for comb in result:
        print(comb)
