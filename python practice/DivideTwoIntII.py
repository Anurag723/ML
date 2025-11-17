def sol(dividend: int, divisor: int) -> int:
    # Handle overflow case
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1  # Integer.MAX_VALUE in Java

    # Determine sign of the result
    flag = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Work with positive long values
    a = abs(dividend)
    b = abs(divisor)

    quotient = 0

    # Perform bitwise division
    for i in range(31, -1, -1):
        if (a >> i) >= b:
            quotient |= (1 << i)
            a -= (b << i)

    return quotient * flag


# Example usage:
if __name__ == "__main__":
    dividend = 10
    divisor = -3
    print(sol(dividend, divisor))
