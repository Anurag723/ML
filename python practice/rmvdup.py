class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) == 0): return 0

        i = 0

        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i] = nums[j]

        return i+1
        

solution = Solution()

# Example input
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# Call the function
k = solution.removeDuplicates(nums)

# Output the result
print("Number of unique elements:", k)
print("Updated list with unique elements:", nums[:k])