from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtrack(s, 0, [], result)
        return result

    def backtrack(self, s: str, index: int, path: List[str], result: List[str]) -> None:
        # If we have 4 parts
        if len(path) == 4:
            if index == len(s):
                result.append(".".join(path))
            return

        # Try 1 to 3 digits
        for length in range(1, 4):
            if index + length > len(s):
                break

            part = s[index:index + length]

            # Skip leading zero numbers
            if len(part) > 1 and part[0] == '0':
                continue

            if int(part) > 255:
                continue

            path.append(part)
            self.backtrack(s, index + length, path, result)
            path.pop()


sol = Solution()
print(sol.restoreIpAddresses("25525511135"))
# Output: ['255.255.11.135', '255.255.111.35']
