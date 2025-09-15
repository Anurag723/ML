class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxcount = 0

        for i in s:
            if i=='(':
                count+=1
                maxcount = max(count,maxcount)

            elif i==')':
                count-=1
        return maxcount
    

# ✅ Runner code
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [
        "(1+(2*3)+((8)/4))+1",  # Expected: 3
        "(1)+((2))+(((3)))",    # Expected: 3
        "1+(2*3)/(2-1)",        # Expected: 1
        "1",                    # Expected: 0
        "",                     # Expected: 0
        "(((())))",             # Expected: 4
        "(a(b(c(d(e)f)g)h)i)",  # Expected: 5
    ]

    for idx, expr in enumerate(test_cases, 1):
        print(f"Test case {idx}: {expr}")
        print(f"Max Depth: {sol.maxDepth(expr)}\n")