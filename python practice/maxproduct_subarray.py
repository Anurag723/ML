class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        mxdp = mndp = result = nums[0]

        for num in nums[1:]:
            temp_mx = max(num, num * mxdp, num * mndp)
            temp_mn = min(num, num * mxdp, num * mndp)

            mxdp = temp_mx
            mndp = temp_mn

            result = max(result, mxdp)

        return result
sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))     # Output: 6
print(sol.maxProduct([-2, 0, -1]))       # Output: 0
print(sol.maxProduct([-2, 3, -4]))       # Output: 24
