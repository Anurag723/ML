class PlusOne:
    def plusOne(self, digits):
        res = []
        carry = 1

        # loop from the last digit to the first
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            res.append(s % 10)
            carry = s // 10

        if carry > 0:
            res.append(carry)

        # reverse the result because we built it backwards
        res.reverse()
        return res


# main
if __name__ == "__main__":
    digits = [9, 9, 9, 9]
    solution = PlusOne()
    result = solution.plusOne(digits)
    print("Result:", result)
