class Solution(object):
    def rotate(self, nums):
        if not nums:  # Handle empty list case
            return
            
        temp = nums.pop(0)
        nums.append(temp)
        return nums

sol = Solution()
my_list = [1, 2, 3, 4, 5]
rotated_list = sol.rotate(my_list)
print("Rotated list:", rotated_list)