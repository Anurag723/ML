from typing import List

class LetterCombination:
    def __init__(self):
        self.digit_to_char = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        self._backtrack(0, [], digits, result)
        return result

    def _backtrack(self, index: int, path: List[str], digits: str, result: List[str]):
        if index == len(digits):
            result.append(''.join(path))
            return

        current_digit = digits[index]
        possible_letters = self.digit_to_char.get(current_digit, "")
        for letter in possible_letters:
            path.append(letter)
            self._backtrack(index + 1, path, digits, result)
            path.pop()  # Backtrack

# Main function to test
def main():
    lc = LetterCombination()
    digits = "23"  # Change this to test other inputs
    combinations = lc.letter_combinations(digits)

    print(f"Letter combinations for '{digits}':")
    for combo in combinations:
        print(combo)

# Run main
if __name__ == "__main__":
    main()
