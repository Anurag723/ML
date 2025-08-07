class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if(len(nums)==0  or len(nums)==1):return 

        k%=len(nums)

        nums[:] = nums[-k:]+ nums[:k+1]


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

solution.rotate(nums, k)
print("Rotated list:", nums)
