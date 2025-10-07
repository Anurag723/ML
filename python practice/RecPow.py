class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1 / x
            N = -N

        return self._power(x, N)

    def _power(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        half = self._power(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


def main():
    sol = Solution()

    result1 = sol.myPow(2.0, 10)
    result2 = sol.myPow(2.0, -2)
    result3 = sol.myPow(5.0, 0)
    result4 = sol.myPow(2.0, -2**31)  # Equivalent to Integer.MIN_VALUE in Java

    print(f"2^10 = {result1}")
    print(f"2^-2 = {result2}")
    print(f"5^0 = {result3}")
    print(f"2^-2147483648 = {result4}")


if __name__ == "__main__":
    main()
