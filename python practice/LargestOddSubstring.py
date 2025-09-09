def largest_odd_number(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i + 1]
    return ""
print(largest_odd_number("1903"))     # Output: "1903"
print(largest_odd_number("4206"))     # Output: ""
print(largest_odd_number("1358"))     # Output: "135"
