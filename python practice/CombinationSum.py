from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self._backtrack(0, ans, [], candidates, target)
        return ans

    def _backtrack(self, start: int, ans: List[List[int]], temp: List[int], candidates: List[int], target: int):
        if target == 0:
            ans.append(list(temp))  # Deep copy
            return
        if start >= len(candidates):
            return

        if candidates[start] <= target:
            temp.append(candidates[start])
            self._backtrack(start, ans, temp, candidates, target - candidates[start])
            temp.pop()

        self._backtrack(start + 1, ans, temp, candidates, target)


# Test case similar to Java main method
if __name__ == "__main__":
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = solution.combinationSum(candidates, target)
    print(f"Combinations summing to {target}: {result}")
