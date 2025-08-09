class Solution(object):
    def singleNum(self, nums):
        res = 0
        for i in nums:res^=i
        return res
    

if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [4, 1, 2, 1, 2]
    print("Input:", nums1)
    print("Single number is:", sol.singleNum(nums1))  # Output: 4

    # Test case 2
    nums2 = [2, 3, 2]
    print("\nInput:", nums2)
    print("Single number is:", sol.singleNum(nums2))  # Output: 3

    # Test case 3
    nums3 = [7]
    print("\nInput:", nums3)
    print("Single number is:", sol.singleNum(nums3))  # Output: 7