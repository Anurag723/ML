class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # Last index of actual elements in nums1
        j = n - 1  # Last index of nums2
        k = m + n - 1  # Last index of nums1 including extra space

        # Merge from the end
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 is not exhausted
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]
m = 3
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print("Merged nums1:", nums1)
