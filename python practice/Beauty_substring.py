def beautySum(s: str) -> int:
    total_beauty = 0
    n = len(s)

    for i in range(n):
        freq = [0] * 26

        for j in range(i, n):
            index = ord(s[j]) - ord('a')
            freq[index] += 1

            max_freq = 0
            min_freq = float('inf')

            for f in freq:
                if f > 0:
                    max_freq = max(max_freq, f)
                    min_freq = min(min_freq, f)

            total_beauty += (max_freq - min_freq)

    return total_beauty

# Example
s = "aabcb"
print("Total beauty of all substrings:", beautySum(s))
