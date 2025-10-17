class PalindromePartition:
    def partition(self, s: str):
        ans = []
        self._sol(0, [], ans, s)
        return ans

    def _sol(self, start, temp, ans, s):
        # If we've reached the end of the string, add the current partition
        if start == len(s):
            ans.append(temp[:])
            return

        # Explore all possible partitions starting from 'start'
        for i in range(start, len(s)):
            if self._is_palindrome(s, start, i):
                temp.append(s[start:i + 1])     # add substring if palindrome
                self._sol(i + 1, temp, ans, s)  # recursive call
                temp.pop()                      # backtrack

    def _is_palindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


# Runner / Test
if __name__ == "__main__":
    obj = PalindromePartition()

    s = "aab"
    result = obj.partition(s)

    print(f"Palindrome partitions of \"{s}\":")
    for part in result:
        print(part)
