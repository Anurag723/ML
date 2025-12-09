class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # ways to reach step 1 and step 2

        for _ in range(3, n + 1):
            a, b = b, a + b

        return b


# Main method equivalent
if __name__ == "__main__":
    sol = Solution()

    n = 10  # you can change this value
    result = sol.climbStairs(n)

    print(f"Number of ways to climb {n} stairs: {result}")
