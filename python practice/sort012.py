class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt0=cnt1=cnt2 = 0
        res = []
        for i in nums:
            if i==0:cnt0+=1
            elif i==1:cnt1+=1
            else:cnt2+=1

        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1
        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2


s = Solution()
nums = [2, 0, 2, 1, 1, 0]
s.sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
