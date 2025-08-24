class Solution:
    def search(self, nums: List[int], target: int) -> int:
        si = 0
        ei = len(nums)-1

        while(si<=ei):
            mid = si+(ei-si)//2

            if(nums[mid]==target):
                return mid

            if(nums[mid]>=nums[si]):
                if(nums[si]<=target<nums[mid]):
                    ei = mid-1

                else:
                    si = mid+1

            else:
                if(nums[mid]<target<=nums[ei]):
                    si = mid+1

                else:
                    ei = mid-1

        return -1
    
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(sol.search([4,5,6,7,0,1,2], 3))  # Output: -1
