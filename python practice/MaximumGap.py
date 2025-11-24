class MaximumGap:
    def maximumGap(self, nums):
        nums.sort()
        temp = 0

        if len(nums) <= 1:
            return 0

        for i in range(1, len(nums)):
            if temp <= nums[i] - nums[i - 1]:
                temp = nums[i] - nums[i - 1]

        return temp


if __name__ == "__main__":
    mg = MaximumGap()

    nums = [3, 6, 9, 1]
    result = mg.maximumGap(nums)

    print("Maximum Gap:", result)
