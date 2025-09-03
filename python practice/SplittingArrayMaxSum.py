from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1

        low, high = max(nums), sum(nums)

        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(nums, mid, k):
                high = mid - 1  # try smaller max sum
            else:
                low = mid + 1  # need to allow a larger max sum

        return low  # smallest possible max sum

    def possible(self, nums: List[int], mid: int, k: int) -> bool:
        count, curr_sum = 1, 0

        for num in nums:
            if curr_sum + num > mid:
                count += 1
                curr_sum = num
                if count > k:
                    return False
            else:
                curr_sum += num

        return True


sol = Solution()
print(sol.splitArray([7,2,5,10,8], 2))  # Output: 18
