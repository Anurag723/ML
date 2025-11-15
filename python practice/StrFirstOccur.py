class StrFirstOccur:

    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i

        return -1


if __name__ == "__main__":
    obj = StrFirstOccur()

    haystack = "hello"
    needle = "ll"

    index = obj.strStr(haystack, needle)

    print("First occurrence index:", index)
