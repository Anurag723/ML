class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        hashi = {0:1}
        tar = 0
        for i in range (len(nums)):
            total += nums[i]
            if total - k in hashi:
                tar += hashi[total-k]
           
            # else:
            hashi[total]= hashi.get(total,0)+1
        return tar
    
if __name__ == "__main__":
    solution = Solution()
    
    nums = [1, 2, 3]
    k = 3
    
    result = solution.subarraySum(nums, k)
    print("Number of subarrays with sum", k, ":", result)