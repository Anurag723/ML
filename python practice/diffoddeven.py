def oddevedif(num) -> int:
    odd = 0
    eve = 0

    for i in num:
        if (i%2==0):
            eve += 1
        else:
            odd += 1

    return odd-eve
num = [1, 2, 3, 4, 5, 6]

print(oddevedif(num))