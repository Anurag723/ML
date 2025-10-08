MOD = 10**9 + 7

class GoodNumber:
    def count_good_numbers(self, n: int) -> int:
        even_positions = (n + 1) // 2  # positions with even indices
        odd_positions = n // 2         # positions with odd indices

        even_part = self.calc(5, even_positions)
        odd_part = self.calc(4, odd_positions)

        return (even_part * odd_part) % MOD

    def calc(self, base: int, exp: int) -> int:
        if exp == 0:
            return 1
        half = self.calc(base, exp // 2)
        result = (half * half) % MOD
        if exp % 2 == 1:
            result = (result * base) % MOD
        return result


# ✅ Runner code
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    solver = GoodNumber()
    result = solver.count_good_numbers(n)
    print(f"Number of good digit strings of length {n} is: {result}")
