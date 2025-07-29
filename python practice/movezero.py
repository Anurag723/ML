def mv(nums):
    left = 0
    for i in range(0,len(nums)):
        if nums[i] != 0:
            nums[left] = nums[i]
            left+=1

    while(left<len(nums)):
        nums[left] = 0
        left+=1

nums = [0, 1, 0, 3, 12]
mv(nums)
print(nums)