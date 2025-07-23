class Solution:
    def insert(self, nums:list[int], target:int)->int:
        if len(nums) is 0:return 0
        beg, end = 0, len(nums)-1

        while(beg<=end):
            mid = beg+(end-beg)//2

            if(nums[mid] == target):
                return mid
            
            elif(nums[mid]<target):
                beg = mid+1

            else:
                end = mid-1

        return beg
    
if __name__ == "__main__":
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    result = solution.insert(nums, target)
    print("Insert Position of", target, ":", result)