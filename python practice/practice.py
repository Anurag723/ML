from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def can_break(substring):
            if substring == "":
                return True
            if substring in memo:
                return memo[substring]

            for i in range(1, len(substring) + 1):
                prefix = substring[:i]
                suffix = substring[i:]

                if prefix in word_set and can_break(suffix):
                    memo[substring] = True
                    return True

            memo[substring] = False
            return False

        return can_break(s)

# Example usage
if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))  # Output: False
