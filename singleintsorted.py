class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        si, ei = 0, len(nums)-1

        while(si<ei):
            mid = si+(ei-si)//2

            if(mid%2==1):
                mid-=1

            if(nums[mid]==nums[mid+1]):
                si = mid+2

            else:
                ei = mid

        return si
    
print(Solution().singleNonDuplicate([1,1,2,3,3]))  # Output: 2
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))  # Output: 10
