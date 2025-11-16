def sol(dividend, divisor):
    # Handle overflow case (equivalent to Java Integer.MIN_VALUE / -1)
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    return dividend // divisor  # integer division

# Example usage
dividend = 10
divisor = -3
print(sol(dividend, divisor))
