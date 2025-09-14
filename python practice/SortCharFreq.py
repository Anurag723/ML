from collections import Counter

class SortFreq:
    def frequency_sort(self, s: str) -> str:
        freq = Counter(s)  # Count frequency of each character
        # Sort items by frequency descending
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = []
        for char, count in sorted_items:
            res.append(char * count)  # Append character count times

        return ''.join(res)


if __name__ == "__main__":
    sorter = SortFreq()
    input_str = "tree"
    output = sorter.frequency_sort(input_str)
    print("Most frequent characters (once):", output)
