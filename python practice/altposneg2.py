class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n  # final result array
        
        pos_index = 0  # even indices for positive numbers
        neg_index = 1  # odd indices for negative numbers
        
        for num in nums:
            if num >= 0:
                res[pos_index] = num
                pos_index += 2
            else:
                res[neg_index] = num
                neg_index += 2
        
        return res
    

sol = Solution()
print(sol.rearrangeArray([1, -1, 2, 3, -2]))  # Output: [1, -1, 2, -2, 3]