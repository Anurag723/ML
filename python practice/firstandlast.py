class Solution(object):
    def searchRange(self, nums:list[int], target:int) ->list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        beg = 0
        end = len(nums)-1

        res = [-1, -1]

        while(beg<=end):
            mid = beg+(end-beg)//2
            if(nums[mid]==target):
                res[0] = mid
                end = mid-1

            elif(nums[mid]<target):
                beg = mid+1

            else:end = mid-1


        beg, end = 0, len(nums) - 1


        while(beg<=end):
            mid = beg+(end-beg)//2
            if(nums[mid]==target):
                res[1] = mid
                beg = mid+1

            elif(nums[mid]<target):
                beg = mid+1

            else:end = mid-1
            
        return res
    
if __name__ == "__main__":
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    result = solution.searchRange(nums, target)
    print("First and Last Position of", target, ":", result)