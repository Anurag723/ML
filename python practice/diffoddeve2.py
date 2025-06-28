def difference_odd_even_index(arr) -> int:
    odd = 0
    eve = 0

    for num in arr:
        if(num%2==0):
            eve+=num

        else:
            odd+=num

    return odd - eve

arr = [1, 2, 3, 4, 5, 6]
print(difference_odd_even_index(arr))