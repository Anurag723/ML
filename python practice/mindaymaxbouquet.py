from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        if len(bloomDay) == m * k:
            return max(bloomDay)

        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.canmake(bloomDay, m, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
    
    def canmake(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        bouquet = flower = 0
        for d in bloomDay:
            if d <= day:
                flower += 1
                if flower == k:
                    bouquet += 1
                    flower = 0
            else:
                flower = 0
            if bouquet >= m:  # small optimization: early exit
                return True
        return False


sol = Solution()
print(sol.minDays([1,10,3,10,2], 3, 1))    # Output: 3
print(sol.minDays([7,7,7,7,12,7,7], 2, 3)) # Output: 12
print(sol.minDays([100,200,300,400], 2, 2))# Output: 300
