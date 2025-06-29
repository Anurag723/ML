def mxpro(numbers) -> int:
    numbers.sort()
    return numbers[-1] * numbers[-2]

arr = [2,8,9,12,18,20]
print(mxpro(arr))