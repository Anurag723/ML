class DecodeWays:
    def num_decodings(self, s: str) -> int:
        return self.decode(s, 0)

    def decode(self, s: str, index: int) -> int:
        # Reached end → valid decoding
        if index == len(s):
            return 1

        # Starts with 0 → invalid
        if s[index] == '0':
            return 0

        # Take one digit
        count = self.decode(s, index + 1)

        # Take two digits if valid
        if index + 1 < len(s):
            two = int(s[index:index + 2])
            if 10 <= two <= 26:
                count += self.decode(s, index + 2)

        return count


if __name__ == "__main__":
    solution = DecodeWays()

    s1 = "226"
    s2 = "12"
    s3 = "06"

    print(f"Input: {s1} → Output: {solution.num_decodings(s1)}")
    print(f"Input: {s2} → Output: {solution.num_decodings(s2)}")
    print(f"Input: {s3} → Output: {solution.num_decodings(s3)}")
