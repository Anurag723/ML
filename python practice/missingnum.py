class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = n*(n+1)/2

        for i in nums:
            sum-=i

        return sum
    
sol = Solution()
my_list = [1, 2, 3, 5, 0]
print(sol.missingNumber(my_list))