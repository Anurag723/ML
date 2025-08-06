class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        pivot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot += 1

        if nums[-1] > nums[0]:
            pivot += 1

        return pivot <= 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.check([3, 4, 5, 1, 2]))  # True
    print(sol.check([2, 1, 3, 4]))     # False
    print(sol.check([1, 2, 3, 4, 5]))  # True