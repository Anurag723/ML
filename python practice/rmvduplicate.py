class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        write_index = 0
        
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[write_index] = num
                write_index += 1

        # Trim the list in-place
        del nums[write_index:]

        return write_index
