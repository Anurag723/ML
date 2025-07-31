def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# Example usage:
print(majorityElement([3, 2, 3]))         # Output: 3
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
