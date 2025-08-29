class Solution:
    def minEatingSpeed(self, piles, h):
        si, ei = 1, max(piles)
        ans = float("inf")

        while si <= ei:
            mid = si + (ei - si) // 2
            k = self.hourly(piles, mid)

            if k <= h:
                ans = mid
                ei = mid - 1
            else:
                si = mid + 1

        return ans

    def hourly(self, piles, mid):
        time = 0
        for pile in piles:
            time += (pile + mid - 1) // mid
        return time
