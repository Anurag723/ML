class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        curr = 0
        for i in nums:
            if i==1:
                curr+=1
                res = max(res, curr)

            else: curr = 0

        return res


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums = [1, 1, 0, 1, 1, 1]
    print("Input:", nums)
    print("Max consecutive 1s:", sol.findMaxConsecutiveOnes(nums))

    # Test case 2
    nums = [1, 0, 1, 1, 0, 1]
    print("\nInput:", nums)
    print("Max consecutive 1s:", sol.findMaxConsecutiveOnes(nums))

    # Test case 3
    nums = [0, 0, 0]
    print("\nInput:", nums)
    print("Max consecutive 1s:", sol.findMaxConsecutiveOnes(nums))

    # Test case 4
    nums = [1, 1, 1, 1]
    print("\nInput:", nums)
    print("Max consecutive 1s:", sol.findMaxConsecutiveOnes(nums))