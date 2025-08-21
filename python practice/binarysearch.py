class solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while(start<=end):
            mid = start+(end-start)//2
            if nums[mid]==target:return mid
            elif(nums[mid]>target):end = mid-1
            else:start = mid+1

        return -1
    
sol = solution()
nums = [1, 3, 5, 7, 9, 11]
target = 7
print(sol.search(nums, target))  # Output: 3
