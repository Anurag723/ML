def add_binary(a: str, b: str) -> str:
    result = []
    
    i = len(a) - 1
    j = len(b) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry == 1:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print("Result:", add_binary(a, b))
