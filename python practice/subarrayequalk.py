class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = {}
        count = prefix = 0

        mp[0] = 1

        for i in nums:
            prefix+=i
            rmv = prefix-k
            count+=mp.get(rmv,0)
            mp[prefix]=mp.get(prefix, 0) + 1

        return count
    


if __name__ == "__main__":
    solution = Solution()
    
    nums = [1, 2, 3]
    k = 3
    
    result = solution.subarraySum(nums, k)
    print("Number of subarrays with sum", k, ":", result)