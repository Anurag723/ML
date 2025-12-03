class LongestValidParan:

    @staticmethod
    def longestValidParentheses(s: str) -> int:
        stack = [-1]  # Base index to help compute lengths
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # No matching '(' → push current index as new base
                    stack.append(i)
                else:
                    # A valid substring ends here
                    max_len = max(max_len, i - stack[-1])

        return max_len


# Runnable main
if __name__ == "__main__":
    test_cases = [
        ")()())",
        "(()())",
        "((()",
        "()(()",
        ""
    ]

    for s in test_cases:
        print(f"Input: {s!r} → Longest Valid: {LongestValidParan.longestValidParentheses(s)}")
