class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s2 = set(nums)
        s1 = list(s2)

        freq = 0

        for i in s1:
            count = nums.count(i)

            if(count>len(nums)/2):freq = i

        return freq
    
if __name__ == "__main__":
    s = Solution()

    # Example test cases
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [1, 1, 1, 3, 3],
        [5, 5, 5, 5, 1, 2, 3],
    ]

    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}: Input: {nums}")
        result = s.majorityElement(nums)
        print(f"Output: {result}\n")
