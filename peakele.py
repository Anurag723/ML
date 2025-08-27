from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        si, ei = 0, len(nums)-1

        while(si<ei):
            mid = si+(ei-si)//2

            if(nums[mid+1]<nums[mid]):
                ei = mid
            else:
                si = mid+1
            
        return si
    

nums = [1, 2, 1, 3, 5, 6, 4]
peak_index = Solution().findPeakElement(nums)
print(f"Peak index: {peak_index}, value: {nums[peak_index]}")
