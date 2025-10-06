class Solution:
    def myAtoi(self, s: str) -> int:
        self.index = 0
        self.sign = 1
        self.result = 0

        s = s.lstrip()  # Remove leading whitespace
        if not s:
            return 0

        def recurse():
            if self.index >= len(s):
                return

            c = s[self.index]

            # Handle optional sign
            if self.index == 0 and (c == '+' or c == '-'):
                self.sign = -1 if c == '-' else 1
                self.index += 1
                recurse()
                return

            # Process digits
            if c.isdigit():
                self.result = self.result * 10 + int(c)

                # Early clamping
                if self.sign * self.result <= -2**31:
                    self.result = -2**31 // self.sign
                    return
                if self.sign * self.result >= 2**31 - 1:
                    self.result = (2**31 - 1) // self.sign
                    return

                self.index += 1
                recurse()
                return

            # Stop recursion on first non-digit
            return

        recurse()

        return max(min(self.sign * self.result, 2**31 - 1), -2**31)
