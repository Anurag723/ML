class UniqueBTree:
    def __init__(self):
        self.memo = []

    def numTrees(self, n: int) -> int:
        self.memo = [0] * (n + 1)
        return self.count(n)

    def count(self, n: int) -> int:
        if n <= 1:
            return 1

        if self.memo[n] != 0:
            return self.memo[n]

        total = 0
        for root in range(1, n + 1):
            total += self.count(root - 1) * self.count(n - root)

        self.memo[n] = total
        return total


# ---------- Runner ----------
if __name__ == "__main__":
    solution = UniqueBTree()

    n = 3  # change this value to test other inputs
    result = solution.numTrees(n)

    print(f"Number of unique BSTs for n = {n} is: {result}")
