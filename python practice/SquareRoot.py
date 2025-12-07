class Squareroot:

    @staticmethod
    def int_sqrt(n):
        low, high, ans = 0, n, 0

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid <= n:
                ans = mid        # mid is a valid candidate
                low = mid + 1    # try to find a larger one
            else:
                high = mid - 1   # mid^2 too big

        return ans


if __name__ == "__main__":
    n = 27
    print(f"Integer sqrt of {n} = {Squareroot.int_sqrt(n)}")
