def canJump(nums):
    furthest = 0
    for i in range(len(nums)):
        if i > furthest:
            return False
        furthest = max(furthest, i + nums[i])
        if furthest >= len(nums):
            return True
    return True


# Test
tst = [3, 2, 1, 0, 4]
print(canJump(tst))  # Expected output: False
