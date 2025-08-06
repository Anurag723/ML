class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k > n

        # Helper function to reverse a portion of the list
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the whole list
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)



nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
