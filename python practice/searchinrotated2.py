class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        si = 0
        ei = len(nums)-1

        while(si<=ei):
            mid = si+(ei-si)//2

            if(nums[mid]==target): return True

            if(nums[si]==nums[mid]==nums[ei]):
                si+=1
                ei-=1

            elif nums[mid]>=nums[si]:
                if nums[si]<=target<nums[mid]:
                    ei = mid-1

                else:
                    si = mid+1

            else:
                if nums[mid]<target<=nums[ei]:
                    si = mid+1

                else:
                    ei = mid-1

        return False
    
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    print(sol.search([2, 5, 6, 0, 0, 1, 2], 0))  # True
    print(sol.search([2, 5, 6, 0, 0, 1, 2], 3))  # False
    print(sol.search([1, 0, 1, 1, 1], 0))        # True
    print(sol.search([1, 1, 3, 1], 3))           # True
    print(sol.search([1, 3, 1, 1, 1], 3))        # True
    print(sol.search([1, 1, 1, 1, 1], 2))        # False
