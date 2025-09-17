class Atoi:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        res = 0
        i = 0
        sign = 1

        # Handle sign
        if s[0] == '+':
            i = 1
        elif s[0] == '-':
            i = 1
            sign = -1
        elif not s[0].isdigit():
            return 0

        # If first char is a digit and no sign was set
        elif s[0].isdigit():
            i = 0

        # Parse digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Overflow check
            if res > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            res = res * 10 + digit
            i += 1

        return res * sign


# ✅ Main test block
if __name__ == "__main__":
    atoi = Atoi()

    test_inputs = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332",
        "+123",
        "",
        "0000012345",
        "+-12",
        "2147483648"
    ]

    for input_str in test_inputs:
        result = atoi.myAtoi(input_str)
        print(f'Input: "{input_str}" -> Output: {result}')
