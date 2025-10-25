class FirstMissing:
    @staticmethod
    def first_missing_positive(nums):
        n = len(nums)
        
        # Step 1: Place each number in its correct position if possible
        i = 0
        while i < n:
            correct_pos = nums[i] - 1
            if 1 <= nums[i] <= n and nums[correct_pos] != nums[i]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1

        # Step 2: Find the first index where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all positions are correct
        return n + 1


# Runner code
if __name__ == "__main__":
    nums1 = [3, 4, -1, 1]
    nums2 = [1, 2, 0]
    nums3 = [7, 8, 9, 11, 12]

    print("First missing positive (Test 1):", FirstMissing.first_missing_positive(nums1))  # Output: 2
    print("First missing positive (Test 2):", FirstMissing.first_missing_positive(nums2))  # Output: 3
    print("First missing positive (Test 3):", FirstMissing.first_missing_positive(nums3))  # Output: 1
