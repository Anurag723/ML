class LongestPalindrome:
    # Helper function to expand around the center
    def expandAroundCenter(self, s, left, right):
        # Expand as long as the characters at left and right are the same
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the valid palindrome substring
        return s[left + 1:right]

    def longestPalindrome(self, s):
        if not s:
            return ""
        
        res = ""
        # Iterate through the string
        for i in range(len(s)):
            # Odd-length palindrome (centered at i)
            palindrome1 = self.expandAroundCenter(s, i, i)
            # Even-length palindrome (centered between i and i+1)
            palindrome2 = self.expandAroundCenter(s, i, i + 1)

            # Update the longest palindrome found
            if len(palindrome1) > len(res):
                res = palindrome1
            if len(palindrome2) > len(res):
                res = palindrome2

        return res

# Testing the class and method
if __name__ == "__main__":
    lp = LongestPalindrome()

    # Test cases
    input1 = "babad"
    input2 = "cbbd"
    input3 = "a"
    input4 = "ac"

    print(f"Longest palindrome in '{input1}': {lp.longestPalindrome(input1)}")  # "bab" or "aba"
    print(f"Longest palindrome in '{input2}': {lp.longestPalindrome(input2)}")  # "bb"
    print(f"Longest palindrome in '{input3}': {lp.longestPalindrome(input3)}")  # "a"
    print(f"Longest palindrome in '{input4}': {lp.longestPalindrome(input4)}")  # "a" or "c"
