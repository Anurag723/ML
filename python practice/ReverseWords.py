class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim and split by any whitespace
        words = s.strip().split()

        # Step 2: Reverse the list and join with a space
        return ' '.join(reversed(words))


sol = Solution()

print(sol.reverseWords("  hello   world  "))     # Output: "world hello"
print(sol.reverseWords("a good   example"))      # Output: "example good a"
print(sol.reverseWords("    "))                  # Output: ""
print(sol.reverseWords("  multiple   spaces "))  # Output: "spaces multiple"
