def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If not found, left will be at the correct insert position
    return left


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # Output: 2

target = 2
print(searchInsert(nums, target))  # Output: 1

target = 7
print(searchInsert(nums, target))  # Output: 4
