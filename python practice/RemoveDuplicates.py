from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        index = 2  # Start from the 3rd position

        for i in range(2, len(nums)):
            # Keep nums[i] only if it's not the same as nums[index - 2]
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1

        return index


# ----------------- Runner Code -----------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    new_len = sol.removeDuplicates(nums)
    print("New length:", new_len)
    print("Modified array:", nums[:new_len])

    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    new_len2 = sol.removeDuplicates(nums2)
    print("\nNew length:", new_len2)
    print("Modified array:", nums2[:new_len2])
