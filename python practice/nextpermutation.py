class Solution(object):
    def nextPermutation(self, nums):
        """
        Rearranges numbers into the next lexicographically greater permutation.
        Modifies nums in-place.
        :type nums: List[int]
        :rtype: None
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray to the right of i
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
sol = Solution()

nums = [1, 2, 3]
sol.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]

nums = [3, 2, 1]
sol.nextPermutation(nums)
print(nums)  # Output: [1, 2, 3]
