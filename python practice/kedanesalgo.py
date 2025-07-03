def kedanealgo(arr) -> int:
    maximum = min(arr)
    curr = 0

    for i in range(len(arr)):
        curr += arr[i]
        
        if maximum < curr:
            maximum = curr

        if curr < 0:
            curr = 0

    return maximum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kedanealgo(arr))