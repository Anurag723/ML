class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if(len(nums)==0  or len(nums)==1):return 

        k%=len(nums)

        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        

    def reverse(self, nums, start, end):
        while(start<end):
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

solution.rotate(nums, k)
print("Rotated list:", nums)
